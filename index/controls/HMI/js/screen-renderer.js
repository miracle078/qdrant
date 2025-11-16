/**
 * HMI Screen Renderer - Renders JSON screen definitions
 * Similar to Ignition Perspective view rendering
 */

class HMIScreenRenderer {
    constructor(containerSelector) {
        this.container = document.querySelector(containerSelector);
        if (!this.container) {
            console.error(`Container not found: ${containerSelector}`);
        }
        this.componentRegistry = this.initializeComponentRegistry();
    }

    /**
     * Initialize the component type registry
     * Maps JSON component types to rendering functions
     */
    initializeComponentRegistry() {
        return {
            'ia.container.flex': this.renderFlexContainer.bind(this),
            'ia.container.coord': this.renderCoordContainer.bind(this),
            'ia.display.label': this.renderLabel.bind(this),
            'ia.display.value': this.renderValue.bind(this),
            'ia.display.table': this.renderTable.bind(this),
            'ia.input.button': this.renderButton.bind(this),
            'ia.input.text-field': this.renderTextField.bind(this),
            'ia.input.numeric-entry-field': this.renderNumericField.bind(this),
            'ia.input.dropdown': this.renderDropdown.bind(this),
            'ia.input.date-time-input': this.renderDateTimeInput.bind(this),
            'ia.chart.pie': this.renderPieChart.bind(this),
            'ia.chart.bar': this.renderBarChart.bind(this),
            'ia.display.alarm-table': this.renderAlarmTable.bind(this),
            'ia.display.state-indicator': this.renderStateIndicator.bind(this)
        };
    }

    /**
     * Load and render a JSON screen definition
     */
    async loadScreen(jsonPath) {
        try {
            const response = await fetch(jsonPath);
            if (!response.ok) {
                throw new Error(`Failed to load screen: ${response.status}`);
            }

            const screenData = await response.json();
            this.renderScreen(screenData);
        } catch (error) {
            console.error('Error loading screen:', error);
            this.renderError(error.message);
        }
    }

    /**
     * Render a screen from JSON data
     */
    renderScreen(screenData) {
        if (!this.container) {
            console.error('No container available for rendering');
            return;
        }

        // Clear existing content
        this.container.innerHTML = '';

        // Handle array of root components or single root
        const components = Array.isArray(screenData) ? screenData : [screenData];

        components.forEach(component => {
            const element = this.renderComponent(component);
            if (element) {
                this.container.appendChild(element);
            }
        });
    }

    /**
     * Render a single component
     */
    renderComponent(component) {
        const renderer = this.componentRegistry[component.type];

        if (!renderer) {
            console.warn(`Unknown component type: ${component.type}`);
            return this.renderUnknownComponent(component);
        }

        return renderer(component);
    }

    /**
     * Apply styles to an element
     */
    applyStyles(element, styles) {
        if (!styles) return;

        Object.keys(styles).forEach(key => {
            // Convert camelCase to kebab-case for CSS properties
            const cssKey = key.replace(/([A-Z])/g, '-$1').toLowerCase();
            element.style[key] = styles[key];
        });
    }

    /**
     * Apply position properties
     */
    applyPosition(element, position) {
        if (!position) return;

        if (position.basis) element.style.flexBasis = position.basis;
        if (position.grow !== undefined) element.style.flexGrow = position.grow;
        if (position.shrink !== undefined) element.style.flexShrink = position.shrink;
    }

    /**
     * Render FlexContainer
     */
    renderFlexContainer(component) {
        const div = document.createElement('div');
        div.className = 'hmi-flex-container';

        const props = component.props || {};

        // Set flex direction
        div.style.display = 'flex';
        div.style.flexDirection = props.direction || 'row';

        // Set alignment
        if (props.justify) div.style.justifyContent = props.justify;
        if (props.alignItems) div.style.alignItems = props.alignItems;
        if (props.alignContent) div.style.alignContent = props.alignContent;
        if (props.wrap) div.style.flexWrap = props.wrap;

        // Apply custom styles
        this.applyStyles(div, props.style);
        this.applyPosition(div, component.position);

        // Set component name as data attribute
        if (component.meta && component.meta.name) {
            div.setAttribute('data-component-name', component.meta.name);
        }

        // Render children
        if (component.children && Array.isArray(component.children)) {
            component.children.forEach(child => {
                const childElement = this.renderComponent(child);
                if (childElement) {
                    div.appendChild(childElement);
                }
            });
        }

        return div;
    }

    /**
     * Render Coordinate Container
     */
    renderCoordContainer(component) {
        const div = document.createElement('div');
        div.className = 'hmi-coord-container';
        div.style.position = 'relative';

        const props = component.props || {};
        this.applyStyles(div, props.style);

        // Render children with absolute positioning
        if (component.children && Array.isArray(component.children)) {
            component.children.forEach(child => {
                const childElement = this.renderComponent(child);
                if (childElement) {
                    childElement.style.position = 'absolute';
                    div.appendChild(childElement);
                }
            });
        }

        return div;
    }

    /**
     * Render Label
     */
    renderLabel(component) {
        const props = component.props || {};
        const label = document.createElement('span');
        label.className = 'hmi-label-component';
        label.textContent = props.text || '';

        this.applyStyles(label, props.style);
        this.applyPosition(label, component.position);

        return label;
    }

    /**
     * Render Value Display
     */
    renderValue(component) {
        const props = component.props || {};
        const div = document.createElement('div');
        div.className = 'hmi-value-display';

        const label = document.createElement('span');
        label.className = 'hmi-value-label';
        label.textContent = props.label || '';

        const value = document.createElement('span');
        value.className = 'hmi-value-number';
        value.textContent = props.value || '0';

        if (props.unit) {
            const unit = document.createElement('span');
            unit.className = 'hmi-value-unit';
            unit.textContent = props.unit;
            value.appendChild(unit);
        }

        div.appendChild(label);
        div.appendChild(value);

        this.applyStyles(div, props.style);
        this.applyPosition(div, component.position);

        return div;
    }

    /**
     * Render Button
     */
    renderButton(component) {
        const props = component.props || {};
        const button = document.createElement('button');
        button.className = 'hmi-button hmi-button-primary';
        button.textContent = props.text || 'Button';

        if (props.enabled === false) {
            button.disabled = true;
        }

        // Add click handler if specified
        if (props.onClick) {
            button.addEventListener('click', new Function(props.onClick));
        }

        this.applyStyles(button, props.style);
        this.applyPosition(button, component.position);

        return button;
    }

    /**
     * Render Text Field
     */
    renderTextField(component) {
        const props = component.props || {};
        const input = document.createElement('input');
        input.type = 'text';
        input.className = 'hmi-input';
        input.placeholder = props.placeholder || '';
        input.value = props.value || '';

        if (props.enabled === false) {
            input.disabled = true;
        }

        this.applyStyles(input, props.style);
        this.applyPosition(input, component.position);

        return input;
    }

    /**
     * Render Numeric Entry Field
     */
    renderNumericField(component) {
        const props = component.props || {};
        const input = document.createElement('input');
        input.type = 'number';
        input.className = 'hmi-input';
        input.value = props.value || '';

        if (props.min !== undefined) input.min = props.min;
        if (props.max !== undefined) input.max = props.max;
        if (props.step !== undefined) input.step = props.step;

        if (props.enabled === false) {
            input.disabled = true;
        }

        this.applyStyles(input, props.style);
        this.applyPosition(input, component.position);

        return input;
    }

    /**
     * Render Dropdown
     */
    renderDropdown(component) {
        const props = component.props || {};
        const select = document.createElement('select');
        select.className = 'hmi-select';

        const options = props.options || [];
        options.forEach(opt => {
            const option = document.createElement('option');
            option.value = opt.value || opt;
            option.textContent = opt.label || opt;
            select.appendChild(option);
        });

        if (props.value) {
            select.value = props.value;
        }

        if (props.enabled === false) {
            select.disabled = true;
        }

        this.applyStyles(select, props.style);
        this.applyPosition(select, component.position);

        return select;
    }

    /**
     * Render Date/Time Input
     */
    renderDateTimeInput(component) {
        const props = component.props || {};
        const input = document.createElement('input');
        input.type = props.mode === 'time' ? 'time' : 'date';
        input.className = 'hmi-input';

        if (props.value) {
            input.value = props.value;
        }

        if (props.enabled === false) {
            input.disabled = true;
        }

        this.applyStyles(input, props.style);
        this.applyPosition(input, component.position);

        return input;
    }

    /**
     * Render Table
     */
    renderTable(component) {
        const props = component.props || {};
        const table = document.createElement('table');
        table.className = 'hmi-table';

        // Render header
        if (props.columns && props.columns.length > 0) {
            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');

            props.columns.forEach(col => {
                const th = document.createElement('th');
                th.textContent = col.label || col.field;
                headerRow.appendChild(th);
            });

            thead.appendChild(headerRow);
            table.appendChild(thead);
        }

        // Render body
        if (props.data && props.data.length > 0) {
            const tbody = document.createElement('tbody');

            props.data.forEach(row => {
                const tr = document.createElement('tr');

                props.columns.forEach(col => {
                    const td = document.createElement('td');
                    td.textContent = row[col.field] || '';
                    tr.appendChild(td);
                });

                tbody.appendChild(tr);
            });

            table.appendChild(tbody);
        }

        this.applyStyles(table, props.style);
        this.applyPosition(table, component.position);

        return table;
    }

    /**
     * Render State Indicator
     */
    renderStateIndicator(component) {
        const props = component.props || {};
        const span = document.createElement('span');

        const state = props.state || 'stopped';
        span.className = `state-indicator state-${state}`;
        span.textContent = props.text || state.toUpperCase();

        this.applyStyles(span, props.style);
        this.applyPosition(span, component.position);

        return span;
    }

    /**
     * Render Alarm Table
     */
    renderAlarmTable(component) {
        const props = component.props || {};
        const container = document.createElement('div');
        container.className = 'alarm-container';

        const alarms = props.alarms || [];
        alarms.forEach(alarm => {
            const alarmDiv = document.createElement('div');
            alarmDiv.className = `alarm alarm-${alarm.priority || 'low'}`;
            if (alarm.active) {
                alarmDiv.classList.add('alarm-active');
            }

            const timestamp = document.createElement('span');
            timestamp.className = 'alarm-timestamp';
            timestamp.textContent = alarm.timestamp || '';

            const message = document.createElement('span');
            message.className = 'alarm-message';
            message.textContent = alarm.message || '';

            alarmDiv.appendChild(timestamp);
            alarmDiv.appendChild(message);
            container.appendChild(alarmDiv);
        });

        this.applyStyles(container, props.style);
        this.applyPosition(container, component.position);

        return container;
    }

    /**
     * Render Pie Chart (simplified)
     */
    renderPieChart(component) {
        const props = component.props || {};
        const div = document.createElement('div');
        div.className = 'hmi-chart-placeholder';
        div.textContent = `Pie Chart: ${props.title || 'Untitled'}`;
        div.style.padding = '20px';
        div.style.border = '2px dashed var(--border-secondary)';
        div.style.borderRadius = 'var(--radius-md)';
        div.style.textAlign = 'center';

        this.applyStyles(div, props.style);
        this.applyPosition(div, component.position);

        return div;
    }

    /**
     * Render Bar Chart (simplified)
     */
    renderBarChart(component) {
        const props = component.props || {};
        const div = document.createElement('div');
        div.className = 'hmi-chart-placeholder';
        div.textContent = `Bar Chart: ${props.title || 'Untitled'}`;
        div.style.padding = '20px';
        div.style.border = '2px dashed var(--border-secondary)';
        div.style.borderRadius = 'var(--radius-md)';
        div.style.textAlign = 'center';

        this.applyStyles(div, props.style);
        this.applyPosition(div, component.position);

        return div;
    }

    /**
     * Render unknown component type
     */
    renderUnknownComponent(component) {
        const div = document.createElement('div');
        div.className = 'hmi-unknown-component';
        div.style.padding = '10px';
        div.style.border = '2px dashed red';
        div.style.backgroundColor = 'rgba(255, 0, 0, 0.1)';
        div.textContent = `Unknown component type: ${component.type}`;
        return div;
    }

    /**
     * Render error message
     */
    renderError(message) {
        if (!this.container) return;

        this.container.innerHTML = `
            <div class="hmi-error" style="
                padding: var(--spacing-lg);
                background: rgba(220, 38, 38, 0.1);
                border: 2px solid var(--alarm-critical);
                border-radius: var(--radius-lg);
                color: var(--alarm-critical);
            ">
                <h3>Error Loading Screen</h3>
                <p>${message}</p>
            </div>
        `;
    }
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HMIScreenRenderer;
}
