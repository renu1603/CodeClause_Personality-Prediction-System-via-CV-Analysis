import csv

test_data = [
    {
        "resume_text": "I am a highly motivated and detail-oriented professional with experience in project management.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am an outgoing and energetic individual with excellent communication skills.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am a creative thinker and problem solver with a passion for innovation.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am empathetic and understanding of others' perspectives.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am organized and keep my work area tidy and efficient.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am curious and enjoy exploring new areas of knowledge.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and show compassion towards others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy meeting new people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am diligent and strive for excellence in my work.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am confident and enjoy taking the lead in group settings.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am focused and determined to achieve my objectives.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and receptive to new ideas.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am supportive and always offer a helping hand.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am outgoing and enjoy socializing with others.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am meticulous and pay attention to the smallest details.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy thinking creatively.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and always take others' feelings into account.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy being the center of attention.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am focused and dedicated to achieving my goals.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and embrace new ideas and perspectives.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and show kindness to others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy spending time with others.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and take my work seriously.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy finding creative solutions.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and treat others with respect.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am outgoing and enjoy socializing with others.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am meticulous and have a keen eye for detail.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy exploring new ideas.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and enjoy working collaboratively.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy being in the spotlight.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am focused and dedicated to achieving my goals.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and receptive to different perspectives.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and empathetic towards others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy spending time with others.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and take my work seriously.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy finding unique solutions to challenges.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and strive to maintain harmony in group settings.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am outgoing and enjoy socializing with others.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am meticulous and have a keen eye for detail.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy exploring new ideas.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and work well in team environments.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am energetic and enjoy being around people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am disciplined and have a strong work ethic.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open to new experiences and love to explore unfamiliar territories.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am empathetic and understanding of others' needs.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and assertive in my communication style.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and reliable in meeting deadlines.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy finding unique solutions to challenges.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and show kindness to others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy spending time with diverse groups of people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am meticulous and pay attention to detail in my work.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy exploring new ideas and concepts.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and enjoy working collaboratively with others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am energetic and thrive in dynamic environments.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am disciplined and focused on achieving my goals.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and receptive to diverse perspectives.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and empathetic towards the needs of others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy taking on leadership roles.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and dependable in meeting my commitments.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy exploring creative solutions.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and value the opinions of others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy building connections with others.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am diligent and detail-oriented in my work.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy thinking outside the box.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and work well in team settings.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am energetic and thrive in high-energy environments.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am disciplined and committed to achieving excellence.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and embrace new ideas and perspectives.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and show compassion to those around me.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy being in social settings.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and accountable for my actions.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy pushing boundaries.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and value cooperation with others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy building relationships.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am meticulous and pay attention to detail in my work.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy exploring new concepts.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and collaborate effectively with others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am energetic and thrive in fast-paced environments.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am disciplined and committed to achieving my goals.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and embrace new ideas and perspectives.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and show empathy towards others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy being the center of attention.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and take my work seriously.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy finding creative solutions.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and always consider the needs of others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy interacting with diverse groups of people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am meticulous and pay attention to detail in my work.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy exploring new ideas and concepts.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and value collaboration with others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am energetic and thrive in social settings.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am disciplined and committed to achieving excellence.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and embrace new ideas and perspectives.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and empathetic towards others' needs.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy being in the spotlight.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and dependable in meeting my commitments.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy exploring creative solutions.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and value the opinions of others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy building connections with others.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am diligent and detail-oriented in my work.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy thinking outside the box.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and work well in team environments.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am energetic and enjoy being around people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and take my work seriously.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open to new experiences and love to explore unfamiliar territories.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am empathetic and understanding of others' needs.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and assertive in my communication style.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and reliable in meeting deadlines.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy finding unique solutions to challenges.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and show kindness to others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy being the center of attention.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am focused and determined to achieve my goals.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and embrace new ideas and perspectives.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am supportive and always offer a helping hand.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am outgoing and enjoy engaging in social activities.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am meticulous and have a keen eye for detail.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy exploring new ideas and concepts.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and work well in team settings.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am energetic and enjoy being around people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am disciplined and always follow through on my commitments.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open to new experiences and love to try new things.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and show empathy towards others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy spending time with diverse groups of people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and take my work seriously.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy finding creative solutions.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and always considerate of others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy being the center of attention.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am focused and determined to achieve my goals.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and embrace new ideas and perspectives.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am supportive and always offer a helping hand.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am outgoing and enjoy engaging in social activities.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am meticulous and have a keen eye for detail.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy exploring new ideas and concepts.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and work well in team settings.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am energetic and enjoy being around people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am disciplined and always follow through on my commitments.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open to new experiences and love to try new things.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and show empathy towards others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy spending time with diverse groups of people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and take my work seriously.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy finding creative solutions.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and always considerate of others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy being the center of attention.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am focused and determined to achieve my goals.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open-minded and embrace new ideas and perspectives.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am supportive and always offer a helping hand.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am outgoing and enjoy engaging in social activities.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am meticulous and have a keen eye for detail.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am imaginative and enjoy exploring new ideas and concepts.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am cooperative and work well in team settings.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am energetic and enjoy being around people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am disciplined and always follow through on my commitments.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am open to new experiences and love to try new things.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am considerate and show empathy towards others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am sociable and enjoy spending time with diverse groups of people.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am responsible and take my work seriously.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am innovative and enjoy finding creative solutions.",
        "personality": "Openness"
    },
    {
        "resume_text": "I am caring and always considerate of others.",
        "personality": "Agreeableness"
    },
    {
        "resume_text": "I am confident and enjoy being the center of attention.",
        "personality": "Extraversion"
    },
    {
        "resume_text": "I am focused and determined to achieve my goals.",
        "personality": "Conscientiousness"
    },
    {
        "resume_text": "I am a highly adaptable individual and can handle stressful situations with ease.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a resilient person and remain calm and composed under pressure.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally stable and can effectively manage my emotions in challenging situations.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a self-assured individual and do not get easily overwhelmed by setbacks.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident problem solver and can handle uncertainties with a positive mindset.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a calm and collected professional, able to maintain composure in high-pressure environments.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a resilient individual and can bounce back from failures and setbacks.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally balanced and can effectively handle stressful situations.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident decision-maker and do not let anxiety impact my choices.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a composed and level-headed professional, able to stay calm in challenging circumstances.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a resilient problem solver, able to tackle obstacles with a positive attitude.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally resilient and can manage stress effectively.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident communicator and can handle difficult conversations with ease.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a composed professional, able to maintain stability in uncertain situations.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally strong and can handle criticism without becoming overly affected.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a self-assured individual and do not let failures deter me from my goals.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a calm and steady professional, able to navigate challenges with resilience.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a resilient problem solver and can find solutions even in stressful situations.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally stable and can maintain a positive outlook even in difficult times.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident leader and can handle crises with composure.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a composed and resilient professional, able to adapt to changing circumstances.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally balanced and can handle pressure with grace.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident decision-maker and do not let anxiety cloud my judgment.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a calm and collected individual, able to navigate challenging situations calmly.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally resilient and can bounce back from adversity.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident communicator and can handle conflicts with composure.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a composed professional, able to maintain stability in high-stress situations.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally strong and do not let negative feedback impact my self-esteem.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a self-assured individual and can handle rejection with resilience.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a calm and level-headed professional, able to navigate challenges with confidence.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally stable and can maintain a positive mindset even in challenging times.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident leader and can handle high-pressure situations with confidence.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a composed and adaptable professional, able to handle uncertainties with ease.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally balanced and can effectively manage stress and anxiety.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident decision-maker and can make sound judgments under pressure.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a calm and composed individual, able to stay focused in challenging situations.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally resilient and can handle setbacks with strength.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident communicator and can handle difficult conversations with composure.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a composed professional, able to maintain stability in turbulent environments.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally strong and can handle criticism without losing confidence.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a self-assured individual and do not let failures define my self-worth.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a calm and steady professional, able to handle challenges with poise.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a resilient problem solver and can find solutions even in high-pressure situations.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally stable and can maintain a positive attitude in challenging circumstances.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident leader and can handle crises with composure and confidence.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a composed and resilient professional, able to adapt to dynamic environments.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally balanced and can handle pressure and stress with resilience.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident decision-maker and do not let anxiety interfere with my choices.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a calm and collected individual, able to navigate challenging situations with confidence.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally resilient and can bounce back from adversity with strength.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a confident communicator and can handle conflicts with diplomacy.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a composed professional, able to maintain stability and composure in high-stress environments.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally strong and do not let negative feedback impact my self-confidence.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a self-assured individual and can handle rejection with resilience and grace.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am a calm and level-headed professional, able to navigate challenges with confidence and poise.",
        "personality": "Neuroticism"
    },
    {
        "resume_text": "I am emotionally stable and can maintain a positive mindset even in challenging circumstances.",
        "personality": "Neuroticism"
    }
]


csv_file = "Dataset/test_dataset.csv"

# Write the above data into new CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["resume_text", "personality"])
    writer.writeheader()
    writer.writerows(test_data)

print(f"Test dataset CSV file '{csv_file}' created successfully.")
