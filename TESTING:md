# Constructly Hub - Testing Documentation

![alt text]( "Overview image of landing page")

🔗 [**Live site**]()

Testing for this project was a continuous and integral part of the development process. The focus was on achieving **highest accuracy and good responsiveness** and **flawless feature functionality**.

---

## Contents

- [User Stories](#user-stories)
- [Automated Testing](#automated-testing)
- [Manual Testing](#manual-testing)
- [Full Testing](#full-testing)
- [Bugs](#bugs)
  - [Known Bugs](#known-bugs)
  - [Solved Bugs](#solved-bugs)

---

### User Stories

| User Story | Test Case | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |

---

### Automated Testing

Automated tools were used throughout the project to ensure code quality and accessibility.

**Google Lighthouse:**

| Page | Performance | Accessibility | Best Practices | SEO | Notes |
| --- | --- | --- | --- | --- | --- |
| Landing Page |   |   |   |   |   |
<!-- | [Another Page] |   |   |   |   |   | -->
| 404 Page |   |   |   |   |   |
<!-- | 401 Page |   |   |   |   |   | -->
<!-- | 503 Page |   |   |   |   |   | -->

**HTML & CSS Validation:**  
Use the **W3C HTML** and **CSS validators** to ensure clean, semantic, and standards-compliant code.  

During HTML validation, some errors appeared in the base template related to the command and commandfor attributes used in the mobile menu button. These attributes are part of the TailwindPlus Elements component system and are not standard HTML5, so the W3C validator flags them as errors. However, they are fully supported by modern browsers and required for the mobile navigation to function correctly.

Since these attributes do not affect performance, accessibility, or user experience, the validation warnings were acknowledged and accepted as a normal consequence of using this component library. I have therefore hidden these specific warnings for future automated testing.

![alt text](documentation/testing/automated-testing/html-js/Screenshot%202025-11-20%20at%2022.13.26.png "base template testing results")

| Page Name                                       | Status                | Notes |
|-------------------------------------------------|-----------------------|-------|
| Base Template (logged out)                      | ⚠️ Accepted Warning   | `command` / `commandfor` are non-HTML5 but required |
| Base Template (logged in)                       | ⚠️ Accepted Warning   | Same as above |
| Landing Page                                    | ✅ Passed             | All errors fixed |
| Login Page                                      | ✅ Passed             | - |
| Sign-Up Page                                    | ✅ Passed             | - |
| Confirm Your Email Address Page                 | ✅ Passed             | - |
| Sign Out Page                                   | ✅ Passed             | - |
| Unable to Confirm Page                          | ✅ Passed             | - |
| Password Reset Request Page                     | ✅ Passed             | - |
| Password Reset Sent Page                        | ✅ Passed             | - |
| Password Reset Done Page                        | ✅ Passed             | - |
| Password Reset Used Link Page                   | ✅ Passed             | - |
| Email Verification Sent Page                    | ✅ Passed             | - |
| Companies Page                                  | ✅ Passed             | - |
| Company Details Page                            | ✅ Passed             | - |
| Create Company Page                             | ✅ Passed             | autocomplete wrong use validated |
| User Companies Page                             | ✅ Passed             | - |
| User Profile Page                               | ✅ Passed             | - |
| Settings Page                                   | ✅ Passed             | - |
| Projects Page                                   | ✅ Passed             | - |
| User Projects Page                              | ✅ Passed             | - |
| Project Details Page                            | ✅ Passed             | All `<div>` / `<p>` validated |
| Project Create Page                             | ✅ Passed             | All `<div>` / `<p>` validated |
| Bids Page                                       | ✅ Passed             | - |
| Remaining Pages                                 | ✅ Passed             | No unresolved issues |


During validation, two warnings appeared related to imported CSS and CSS variables. These are caused by the @import "tailwindcss"; line, as Tailwind is generated dynamically and the W3C validator cannot inspect imported stylesheets or statically check CSS variables. These warnings are expected and do not affect functionality or performance.

**JavaScript Validation:**  
No issues in JS code.

![alt text](documentation/testing/automated-testing/html-js/Screenshot%202025-11-21%20at%2010.10.45.png "JShint results")

**Python**

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | Linting Screenshot | Warnings |
|------|--------------------|----------|
| companies-admin | ![companies-admin](documentation/testing/automated-testing/python/companies-admin.png "companies-admin") | — |
| companies-forms | ![companies-forms](documentation/testing/automated-testing/python/companies-forms.png "companies-forms") | — |
| companies-models | ![companies-models](documentation/testing/automated-testing/python/companies-models.png "companies-models") | — |
| companies-urls | ![companies-urls](documentation/testing/automated-testing/python/companies-urls.png "companies-urls") | — |
| companies-views | ![companies-views](documentation/testing/automated-testing/python/companies-views.png "companies-views") | — |
| settings | ![settings](documentation/testing/automated-testing/python/settings.png "settings") | Line 114, 117, 120, 123 too long |
| global-urls | ![global-urls](documentation/testing/automated-testing/python/global-urls.png "global-urls") | — |
| landing-urls | ![landing-urls](documentation/testing/automated-testing/python/landing-urls.png "landing-urls") | — |
| landing-views | ![landing-views](documentation/testing/automated-testing/python/landing-views.png "landing-views") | — |
| projects-admin | ![projects-admin](documentation/testing/automated-testing/python/projects-admin.png "projects-admin") | — |
| projects-forms | ![projects-forms](documentation/testing/automated-testing/python/projects-forms.png "projects-forms") | — |
| projects-models | ![projects-models](documentation/testing/automated-testing/python/projects-models.png "projects-models") | — |
| projects-urls | ![projects-urls](documentation/testing/automated-testing/python/projects-urls.png "projects-urls") | — |
| projects-views | ![projects-views](documentation/testing/automated-testing/python/projects-views.png "projects-views") | Line 85 & 158 too long |
| bids-admin | ![bids-admin](documentation/testing/automated-testing/python/bids-admin.png "bids-admin") | — |
| bids-forms | ![bids-forms](documentation/testing/automated-testing/python/bids-forms.png "bids-forms") | — |
| bids-models | ![bids-models](documentation/testing/automated-testing/python/bids-models.png "bids-models") | — |
| bids-urls | ![bids-urls](documentation/testing/automated-testing/python/bids-urls.png "bids-urls") | — |
| bids-views | ![bids-views](documentation/testing/automated-testing/python/bids-views.png "bids-views") | — |
| userprofile-admin | ![userprofile-admin](documentation/testing/automated-testing/python/userprofile-admin.png "userprofile-admin") | — |
| userprofile-forms | ![userprofile-forms](documentation/testing/automated-testing/python/userprofile-forms.png "userprofile-forms") | — |
| userprofile-models | ![userprofile-models](documentation/testing/automated-testing/python/userprofile-models.png "userprofile-models") | — |
| userprofile-urls | ![userprofile-urls](documentation/testing/automated-testing/python/userprofile-urls.png "userprofile-urls") | — |
| userprofile-views | ![userprofile-views](documentation/testing/automated-testing/python/userprofile-views.png "userprofile-views") | — |

**Accessibility Testing:**  
Use the **WAVE** tool to ensure compliance with accessibility standards.

---

### Manual Testing

Extensive manual testing ensures consistent layout, functionality, and responsiveness across devices and browsers.

**Common to all pages:**

| Test # | Test Description | Expected Result | Actual Result | Pass/Fail |
| --- | --- | --- | --- | --- |

---

### Main Page Testing

| Test # | Test Description | Expected Result | Actual Result | Pass/Fail |
| --- | --- | --- | --- | --- |

---

### Form Testing (Multi-Step or Single-Step)

| Test # | Test Description | Expected Result | Actual Result | Pass/Fail |
| --- | --- | --- | --- | --- |

---

### Full Testing

All major flows, features, and responsiveness were tested across:

<!-- - Desktop, tablet, and mobile devices. -->
<!-- - Browsers: **Chrome, Firefox, Safari, Edge, Opera**. -->

---

## Bugs

### Known Bugs
None

### Solved Bugs
Prettier crash deletes staged files - removed from the set-up.

Main closing tag in footer on home page causng footer take container width. Moved main closing tag outside of footer on top. 

Login and signup pages didn’t show form errors. Fixed by adding blocks for form.non_field_errors and field-specific errors.

Update button for companies had a wrong attributes so Update button did not work on iPhone.
---

[Back to README.md](README.md) • [Back to Top](#constructly-hub---testing-documentation)