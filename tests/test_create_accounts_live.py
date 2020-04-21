from screen_pages.group import Group

def test_create_live_account_boy(app):
    app.sign_up.open_abcmouse_web_page("https://www.abcmouse.com/abt/subscription")  # Update URL QTEST!
    app.sign_up.submit_and_confirm_email("sitetimer@live.test") ##### Change Email Credentials!
    app.sign_up.submit_and_confirm_password("test123")
    app.payment_info.submit_cc_live(cardholder="Test Alex Ko")
    app.sign_up.click_submit_button()

    ##### Annual Subscription Page
    app.sign_up.select_no_thanks_annual_subscription()
    app.sign_up.close_annual_subscription_pop_up()

    ###### Assessment Subscription Page
    app.sign_up.select_no_thanks_free_trial_assessment_subscription()

    assert app.sign_up.thank_you_text()

    ###### ON-BOARDING PAGE
    app.sign_up.click_submit_continue_registration_button()
    app.onboarding.welcome_page_click_get_started_button()
    app.onboarding.survey_click_continue_buttons()
    app.onboarding.input_parent_name(parent_first_name="AK Test", parent_family_name="Ko Test")
    ##### (grade Levels' IDs: [toddler-time] [preschool] [pre-k] [kindergarten] [first-grade] [second-grade]
    app.onboarding.create_child_profile(child_name="B_1", gender="M", academic_level="first-grade")
    app.onboarding.choose_avatar(avatar="boy_avatar03")  #####   |  boy_avatar03  |  girl_avatar03
    app.onboarding.choose_hamster_and_fish(hamster="hamster-3", fish="fish-3", hamster_name="My Ham-StAr")
    app.onboarding.skip_video()
    app.onboarding.go_to_shp()
    assert app.onboarding.mouse_pop_up()
    assert app.driver.current_url == "https://www.abcmouse.com/html5#abc/student_home"