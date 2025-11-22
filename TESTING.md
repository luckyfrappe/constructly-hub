# Constructly Hub - Testing Documentation

![Landing page](documentation/testing/manual-testing/landing.png "Overview image of landing page")

🔗 [**Live site**](https://constructly-hub-ee092254593a.herokuapp.com/)

Testing for this project was a continuous part of the development process.

## Contents

- [User Stories](#user-stories)
- [Automated Testing](#automated-testing)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
  - [Known Bugs](#known-bugs)
  - [Solved Bugs](#solved-bugs)

---

### User Stories

Below is a summary confirming that each user story was manually tested across desktop and mobile devices.

**Story 1: Guest Access & Restricted Features**

**Test Summary:**  
The platform was tested as an unauthenticated guest. Navigation from the landing page to the subcontractors list works, and all restricted features (bidding, creating projects, creating companies) are hidden. No authentication-only buttons appear.

**Result:** Pass  

![Guest Access Test](documentation/testing/manual-testing/guest-companies.png)

**Story 2: User Registration & Login**

**Test Summary:**  
User registration and login were tested via Django AllAuth. Users can sign up and sign in successfully. Incorrect login credentials trigger the correct error messages. Session remains active until logout.

**Result:** Pass  

![Auth Test](documentation/testing/manual-testing/sign-in.png)
![Auth Test](documentation/testing/manual-testing/sign-up.png)

**Story 4: Create New Project**

**Test Summary:**  
A logged-in client can create a new project, view it in the projects list. All required fields validate correctly. Deadlines, budget, and descriptions save and display as expected.

**Result:** Pass  

![Create Project Test](documentation/testing/manual-testing/create-project.png)

**Story 6: Review Bids & Award Winner**

**Test Summary:**  
Bid comparison was tested using multiple test bids. Client can view all bids, see price and delivery info, and select a winning bid. Project status updates to *Completed*, and other bids correctly switch to *Rejected*.

**Result:** Pass  

![Bid Selection Test](documentation/testing/manual-testing/review-bids.png)

**Story 5: CRUD Companies**

**Test Summary:**  
Users can view all companies, create new ones, edit details, update logos, and delete their own companies. Owner-only restrictions and permission checks work correctly. Company cards show logo, name, location, and owner info.

**Result:** Pass  

![CRUD Companies Test](documentation/testing/manual-testing/all-companies.png)
![CRUD Companies Test](documentation/testing/manual-testing/crud.png)
![CRUD Companies Test](documentation/testing/manual-testing/create-company.png)

**Story 7: Filter User-Owned Companies**

**Test Summary:**  
The “Your Companies” page only displays companies owned by the logged-in user. Layout, pagination, cards, and owner info display correctly. 

**Result:** Pass  

![User Companies Test](documentation/testing/manual-testing/my-companies.png)

**Story 9: Admin & Project Management**

**Test Summary:**  
Admin dashboard lists all users and projects. Admin permissions allow editing and deleting records. Non-admin users are correctly blocked from accessing the admin area.

**Result:** Pass  

![Admin Test](documentation/testing/manual-testing/django-admin.png)

**Story 10: Bidding**

**Test Summary:**  
Subcontractors can browse open projects, submit bids with price, duration, and comments. Bids appear on their “Your Bids” page. Bidding is blocked on completed projects, and validation works correctly.

**Result:** Pass  

![Bidding Test](documentation/testing/manual-testing/all-projects.png)
![Bidding Test](documentation/testing/manual-testing/place-bid.png)

---

### Automated Testing

Automated tools were used throughout the project to ensure code quality and accessibility.

**Google Lighthouse:**

| Page | Screenshot |
|------|------------|
| 404 Page | ![404 page](documentation/testing/automated-testing/lighthouse/404.png "404") |
| All Companies (Guest View) | ![All companies guest](documentation/testing/automated-testing/lighthouse/all-companies-guest-view.png "all-companies-guest-view") |
| All Companies (Signed In) | ![All companies signed in](documentation/testing/automated-testing/lighthouse/all-companies-signed-in.png "all-companies-signed-in") |
| All Projects | ![All projects](documentation/testing/automated-testing/lighthouse/all-projects.png "all-projects") |
| Change Your Password | ![Change password](documentation/testing/automated-testing/lighthouse/change-your-password.png "change-your-password") |
| Company Details | ![Company details](documentation/testing/automated-testing/lighthouse/company-details.png "company-details") |
| Confirm Email | ![Confirm email](documentation/testing/automated-testing/lighthouse/confirm-email.png "confirm-email") |
| Create Company | ![Create company](documentation/testing/automated-testing/lighthouse/create-company.png "create-company") |
| Create Project | ![Create project](documentation/testing/automated-testing/lighthouse/create-project.png "create-project") |
| Forgot Password | ![Forgot password](documentation/testing/automated-testing/lighthouse/forgot-password.png "forgot-password") |
| Landing Page (Guest View) | ![Landing guest](documentation/testing/automated-testing/lighthouse/landing-page-guest-view.png "landing-page-guest-view") |
| Landing Page (Signed In) | ![Landing signed in](documentation/testing/automated-testing/lighthouse/landing-signed-in.png "landing-signed-in") |
| My Bids | ![My bids](documentation/testing/automated-testing/lighthouse/my-bids.png "my-bids") |
| My Companies | ![My companies](documentation/testing/automated-testing/lighthouse/my-companies.png "my-companies") |
| My Projects | ![My projects](documentation/testing/automated-testing/lighthouse/my-projects.png "my-projects") |
| Profile Settings | ![Profile settings](documentation/testing/automated-testing/lighthouse/profile-settings.png "profile-settings") |
| Profile | ![Profile](documentation/testing/automated-testing/lighthouse/profile.png "profile") |
| Project Review | ![Project review](documentation/testing/automated-testing/lighthouse/project-review.png "project-review") |
| Reset Password Sent | ![Reset password sent](documentation/testing/automated-testing/lighthouse/reset-password-sent.png "reset-password-sent") |
| Sign In | ![Sign in](documentation/testing/automated-testing/lighthouse/sign-in.png "sign-in") |
| Sign Out | ![Sign out](documentation/testing/automated-testing/lighthouse/sign-out.png "sign-out") |
| Sign Up | ![Sign up](documentation/testing/automated-testing/lighthouse/sign-up.png "sign-up") |
| Verify Email | ![Verify email](documentation/testing/automated-testing/lighthouse/verify-email.png "verify-email") |

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

During validation, two warnings appeared related to imported CSS and CSS variables. These are caused by the @import "tailwindcss".

Autoprefixer: This tool was used to automatically add vendor prefixes to the CSS properties, ensuring the website's styles render correctly across a wide range of browsers. This step was essential for maintaining a consistent look and feel, even for older browser versions.

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

WAVE was used to check accessibility on all publicly available pages.  
Because WAVE cannot access authenticated sessions, private pages (projects, bids,
settings, companies, etc.) could not be tested directly.

However, all private pages use the same base template for layout, navigation,
contrast, and typography. Since the base template passed WAVE checks without
critical errors, the same accessibility level is consistently applied across the
entire platform.

![Companies Guest](documentation/testing/automated-testing/wave/companies-guest.png "Companies Guest")
![Landing Page](documentation/testing/automated-testing/wave/landing-page-guest.png "Landing Page")
![Reset](documentation/testing/automated-testing/wave/reset.png "Reset")
![Sign In](documentation/testing/automated-testing/wave/sign-in.png "Sign In")
![Sign Up](documentation/testing/automated-testing/wave/sign-up.png "Sign Up")

---

## Manual Testing

Extensive manual testing ensures consistent layout, functionality, and responsiveness across devices and browsers.

**1. Global Layout & Navigation**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 001 | Header & footer render on all pages | Visible, consistent across pages | pass |
| 002 | Navigation links work | All nav links go to correct pages | pass |
| 003 | Mobile menu works | Opens/closes correctly | pass |
| 004 | Responsive layout | All pages adjust on mobile/tablet/desktop | pass |
| 005 | Avatar + fallback images load | Custom avatar or fallback shown | pass |
| 006 | Flash messages | Display correctly + can be dismissed | pass |
| 007 | No console errors | No JS errors in browser console | pass |


**2. Authentication (Basic)**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 101 | Sign-in/out links work | Redirect to login/logout as expected | pass |
| 102 | Auth-required pages redirect | Unauthenticated users cannot access restricted pages | pass |


**3. Landing Page**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 201 | Hero section loads | Heading, text, call-to-action visible | pass |
| 202 | CTA button works | Redirects correctly depending on auth state | pass |


**4. 404 Page**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 301 | 404 content loads | 404 title, text, image | pass |
| 302 | Back button | Returns to previous page | pass |
| 303 | Responsive layout | Works on all screen sizes | pass |


**5. Profile Page**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 401 | Profile info loads | Name, email, bio, avatar | pass |
| 402 | Edit button | Opens settings page | pass |
| 403 | Delete account modal | Opens and closes correctly | pass |
| 404 | Responsive layout | Stacks correctly on mobile | pass |


**6. Settings Page**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 501 | Form loads with user data | All fields pre-filled | pass |
| 502 | Fields editable | Name, email, phone, bio | pass |
| 503 | Validation errors | Required + invalid inputs show error | pass |
| 504 | Avatar upload (FilePond) | Upload, preview, validation | pass |
| 505 | Save button | Updates profile | pass |
| 506 | Back button | Returns to profile | pass |


**7. Projects Page (List)**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 601 | Projects load or empty state | Cards show OR “No projects found” | pass |
| 602 | Card info visible | Title, location, budget, status, deadline | pass |
| 603 | Clicking card | Opens correct project detail | pass |
| 604 | Pagination | Next/Prev & page numbers work | pass |
| 605 | Responsive layout | Grid adjusts between screen sizes | pass |


**8. Project Detail Page**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 701 | Project details load | Title, budget, location, description | pass |
| 702 | Client info visible | Name, avatar, contact | pass |
| 703 | Bids section (client) | Shows bids if any | pass |
| 704 | Bid form (contractor) | Shows only when project open | pass |
| 705 | Bid submission | Valid form submits correctly | pass |
| 706 | Responsive layout | Works on all breakpoints | pass |


**9. Create Project**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 801 | Form loads | All fields visible | pass |
| 802 | Required fields validation | Title, location, description, budget, deadline | pass |
| 803 | Save button | Creates project | pass |
| 804 | Cancel button | Goes back | pass |


**10. Your Companies Page**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 901 | Page loads | Company cards visible | pass |
| 902 | Card link | Opens correct company detail | pass |
| 903 | Add New Company card | Appears + links correctly | pass |
| 904 | Pagination | Works correctly | pass |
| 905 | Responsive grid | 1 column mobile, 3 columns desktop | pass |


**11. Create Company**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 1001 | Form loads (authenticated) | Visible only with user profile | pass |
| 1002 | Required fields validation | Company name, role, description, location, services | pass |
| 1003 | Logo upload | FilePond preview + validation | pass |
| 1004 | Save button | Creates company | pass |
| 1005 | Cancel button | Goes back | pass |


**12. Company Detail Page**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 1101 | Company details load | Logo, name, location, services | pass |
| 1102 | Website link | Opens in new tab | pass |
| 1103 | Edit/Delete (owner only) | Shown only to company owner | pass |
| 1104 | Edit modal works | Loads data + updates | pass |
| 1105 | Delete modal | Opens and deletes correctly | pass |
| 1106 | Responsive layout | Works across breakpoints | pass |


**13. Your Bids Page**

| Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 1201 | Page loads | Bids or empty message shown | pass |
| 1202 | Bid cards show correct info | Title, price, deadline, status | pass |
| 1203 | Clicking a bid | Opens corresponding project | pass |
| 1204 | Pagination | Works correctly | pass |
| 1205 | Responsive layout | Works on mobile and desktop | pass |

**14. Cross-Browser & Device Quick Testing**

These core features were manually tested on **Chrome**, **Safari**, **Firefox**, **Edge**, and real devices (**iPhone 16**, **iPad Air**).

| Test # | Test Description | Browsers Tested | Devices Tested | Result |
|-------|------------------|------------------|----------------|--------|
| 950 | Pages load without layout breaking | Chrome, Safari, Firefox, Edge | iPhone, iPad | pass |
| 951 | Navigation works (Header, Logo, Footer links) | Chrome, Safari, Firefox, Edge | iPhone, iPad | pass |
| 952 | Mobile menu works (open/close) | Chrome, Safari, Firefox, Edge | iPhone | pass |
| 953 | Forms render correctly (inputs, validation messages) | Chrome, Safari, Firefox, Edge | iPhone, iPad | pass |
| 954 | FilePond loads and accepts images | Chrome, Safari | iPhone, iPad | pass |
| 955 | Pagination buttons work and stay responsive | Chrome, Safari, Firefox | iPhone, iPad | pass |
| 956 | Cards (projects/companies/bids) display correctly + clickable | Chrome, Safari, Firefox, Edge | iPhone, iPad | pass |
| 957 | Modals open/close smoothly (edit/delete) | Chrome, Safari, Firefox | iPad | pass |
| 958 | No blocking console errors | Chrome | - | pass |
| 959 | Dark/light backgrounds + SVG/FontAwesome icons render correctly | Chrome, Safari, Firefox | iPhone, iPad | pass |

## Bugs

### Known Bugs
None

### Solved Bugs

Main closing tag in footer on home page causng footer take container width. Moved main closing tag outside of footer on top. 

Login and signup pages didn’t show form errors. Fixed by adding blocks for form.non_field_errors and field-specific errors.

Update button for companies had a wrong attributes so Update button did not work on iPhone.

---

[Back to README.md](README.md) • [Back to Top](#constructly-hub---testing-documentation)