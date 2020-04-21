

def test_create_paypal_free_trial_girl_and_boy(app):
    app.sign_up.open_abcmouse_web_page("https://ep.qtest.abcmouse.com/abt/subscription")  # Update URL QTEST!
    app.sign_up.submit_and_confirm_email("ppal1@ep.test") ##### Change Email Credentials!
    app.sign_up.submit_and_confirm_password("test123")
    app.payment_info.submit_paypal_qtest()

    #### [NEW] Check here to agree that, after your free trial month, you will be charged $9.95.
    # app.credit_info.check_to_agree()

    app.sign_up.click_submit_button()
    app.sign_up.click_submit_button()

    ##### Annual Subscription Page
    app.sign_up.select_no_thanks_annual_subscription()
    app.sign_up.close_annual_subscription_pop_up()
    ###### Assessment Subscription Page
    app.sign_up.select_no_thanks_free_trial_assessment_subscription()
    assert app.sign_up.thank_you_text()
    app.sign_up.click_submit_continue_registration_button()
    ###### ON-BOARDING PAGE
    app.onboarding.welcome_page_click_get_started_button()
    app.onboarding.survey_click_continue_buttons()
    app.onboarding.input_parent_name(parent_first_name="AK Test", parent_family_name="Ko Test")
    ##### (grade Levels' IDs: [toddler-time] [preschool] [pre-k] [kindergarten] [first-grade] [second-grade]
    app.onboarding.create_child_profile(child_name="G1(ppal1)", gender="F", academic_level="preschool")
    app.onboarding.choose_avatar(avatar="girl_avatar03")  #####  girl_avatar01  |  girl_avatar16
    app.onboarding.choose_hamster_and_fish(hamster="hamster-1", fish="fish-1", hamster_name="My Ham-StAr")
    app.onboarding.skip_video()

    app.onboarding.add_child()
    ##### (grade Levels' IDs: [toddler-time] [preschool] [pre-k] [kindergarten] [first-grade] [second-grade]
    app.onboarding.create_child_profile(child_name="B2", gender="M", academic_level="kindergarten")
    app.onboarding.choose_avatar(avatar="boy_avatar07")  #####   |  boy_avatar03  |  girl_avatar03
    app.onboarding.choose_hamster_and_fish(hamster="hamster-2", fish="fish-2", hamster_name="My Ham-StAr")
    app.onboarding.go_to_shp()
    assert app.onboarding.mouse_pop_up()