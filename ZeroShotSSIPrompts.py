def p1(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""As a clinical expert, your role is to determine 
                     if a patient has a surgical site infection (SSI) or postoperative infection."""})
    messages.append({"role": "user", "content": f"""Classify the following clinical note as 'Yes' if 
                     the corresponding patient has a surgical site infection. Otherwise output 'No'. 
                     Clinical note: {note_text}"""})
    return messages

def p2(note_text):
    messages = []
    messages.append({"role": "system", "content": f"""Your responsibility is to analyze clinical notes and
                     ascertain whether they describe a surgical site infection (SSI) based on the 
                     definitions provided by the National Surgical Quality Improvement Program (NSQIP).
                     The NSQIP definitions for a surgical site infection are:
                     
                     Definition 1: Superficial Incisional SSI is an infection that involves only skin or 
                     subcutaneous tissue of the surgical incision.                    

                     Criteria for Definition 1: An infection that occurs within 30 days after the primary 
                     procedure AND the infection involves only skin or subcutaneous tissue of the 
                     incision/sites integral to the Primary Procedure AND at least ONE of the following A, B, C, or D:
                     A. Purulent drainage, with or without laboratory confirmation, from the superficial incision.
                     B. Organisms isolated from an aseptically obtained culture of fluid or tissue from the 
                     superficial incision.
                     C. Superficial incision is deliberately opened by the surgeon in the presence of at least 
                     one of the following signs or symptoms of infection: pain or tenderness, localized swelling, 
                     redness, heat.
                     D. Diagnosis of superficial incisional SSI by the physician or advanced provider.

                     Scenarios to clarify for Definition 1:
                     - Superficial SSI which occurs at a drain site, in which the drain was placed during 
                     the primary procedure.
                     - If patient meets criteria A or D, a negative culture of the surgical incision will 
                     not affect the assignment of this occurrence.
                     - If a diagnosis of cellulitis is treated with oral/IV/IM antimicrobial therapy, 
                     this would be considered a diagnosis of an infection, meeting criterion D.
                     - Documentation of green drainage (unless attributed to a bile leak) identified in 
                     the superficial incision site meets criterion A.
                     - Documentation of a phlegmon identified in the superficial incision site meets criterion A.
                     - Documentation of an abscess identified in the superficial incision site meets criterion A.
                     - If antimicrobials are ordered with an indication for possible/probable infection, 
                     this would meet Criterion D, as a diagnosis of infection.

                     Definition 2: Deep Incisional SSI is an infection which involves deep soft tissues. 
                     Deep soft tissues are typically any tissue beneath skin and immediate subcutaneous fat, 
                     for example fascial and muscle layers.

                     Criteria for Definition 2: An infection that occurs at the surgical site/sites integral 
                     to the Primary Procedure within 30 days after the primary procedure AND involves deep 
                     soft tissues AND at least ONE of the following:
                     A. Purulent drainage or a positive culture from the deep incision but not from the 
                     organ/space component of the surgical site.
                     B. A deep incision spontaneously dehisces or is deliberately opened by a surgeon when 
                     the patient has at least one of the following signs or symptoms: fever (> 38⁰ C), localized pain, 
                     or tenderness, unless the site is culture-negative.
                     C. An abscess or other evidence of infection involving the deep incision is found on direct 
                     examination, during reoperation, or by radiologic examination.
                     D. Diagnosis of a deep incision SSI by a physician or advanced provider.

                     Scenarios to clarify for Definition 2:
                     - Diagnosis of pharyngitis in association with purulent drainage after oral surgery.
                     - Documentation of green drainage (unless attributed to a bile leak) identified in the 
                     deep layers of the incision meets criterion A.
                     - Documentation of a phlegmon identified in the deep layers of the incision site meets criterion A.
                     - Documentation of an abscess identified in the deep layers of the incision site meets criterion A.
                     - If antimicrobials are ordered with an indication for possible/probable infection, this would meet 
                     Criterion D, as a diagnosis of infection.

                     Definition 3: Organ/Space SSI is an infection that involves any part of the 
                     anatomy (e.g., organs or spaces), other than the incision, which was opened or manipulated during 
                     the primary procedure.

                     Criteria for Definition 3: An infection that occurs within 30 days after the primary procedure 
                     AND involves any of the anatomy (e.g., organs or spaces), other than the incision, which was 
                     opened or manipulated during the primary procedure, including sites integral to the primary 
                     procedure, AND at least ONE of the following:
                     A. Purulent drainage from a drain that is placed through a stab wound into the organ/space.
                     B. Organisms isolated from an aseptically obtained culture of fluid or tissue in the organ/space.
                     C. An abscess or other evidence of infection involving the organ/space that is found on direct 
                     examination, during reoperation, or by radiologic examination.
                     D. Diagnosis of an organ/space SSI by a physician or advanced provider.

                     Scenarios to clarify for Definition 3:
                     - For Gastrointestinal (GI) Procedures: Anastomotic/staple line leaks involving the GI tract.
                     - Injury to intestine (e.g., enterotomy, iatrogenic injury, perforation).
                     - For Genitourinary (GU) Procedures: Anastomotic/staple line leaks or injury (e.g., perforation) 
                     involving the GU tract with an attributed elevated WBC or fever or other evidence of infection.
                     - Documentation of green drainage (unless attributed to a bile leak) identified in the 
                     organ/space meets criterion A.
                     - Documentation of a phlegmon identified in the organ/space meets criterion A.
                     - Documentation of an abscess identified in the organ/space meets criterion A.
                     - If antimicrobials are ordered with an indication for possible/probable infection, 
                     this would meet Criterion D, as a diagnosis of infection."""})
    messages.append({"role": "user", "content": f"""Does the following clinical note describe a surgical site infection 
                     as specified by at least one of the NSQIP definitions? Answer either 'Yes' or 'No'!                                          
                     Clinical note: {note_text}"""})
    return messages
