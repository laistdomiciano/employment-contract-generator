graph TD
    A[Requirement Gathering] --> B[Design]
    B --> C[UI Design]
    B --> D[Backend Design]
    B --> E[Database Design]
    C --> F[Frontend Development]
    D --> G[Backend Development]
    E --> H[Database Setup]
    F --> I[Form Validation]
    G --> J[Template Filling Logic]
    H --> K[Integration]
    I --> L[Testing]
    J --> L
    K --> L
    L --> M[Deployment]

    subgraph Frontend
        F --> I
    end

    subgraph Backend
        G --> J
        J --> K
    end

    subgraph Database
        E --> H
    end

    subgraph Integration
        K
    end

    subgraph Testing
        L
    end

    subgraph Deployment
        M
    end
