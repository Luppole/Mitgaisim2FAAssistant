היי לכולם! 
לאחרונה התחלתי להשתמש באתר של מתגייסים (יחידת מיט"ב) כדי להסתכל על ציונים ופרופיל רפואי, וגם כדי להתכונן לצו הראשון. דבר שנורא הפריע לי באתר הוא העובדה שיש 2FA בכל כניסה (גם creds וגם מייל אימות). תהליך ה-2FA עלול לגזול כמה שניות טובות במקרה הטוב ואפילו דקה - שתיים במקרה הרע (במידה והמייל שנשלח מהאתר מסווג כספאם או שסתם לוקח לאדם ממוצע בערך דקה לאתר מייל, לפתוח, להעתיק ולהדביק סדרת מספרים ולהתחבר). בערב שבת אחד החלטתי שאני רוצה לייעל את כל התהליך הזה, אז חקרתי קצת על Google API, בדגש על Gmail API, ובעזרת האינטרנט המופלא ו-Github Copilot (באדיבות גיטהאב סטודנט האדיבים) - כתבתי את הקוד הזה, שבלחיצה אחת מעתיק את הקוד, ומה שנשאר הוא להדביק. 
אני כרגע נמנע מלעשות אוטומציה מלאה עם Webdriver לכל תהליך הסיסמאות, אך הרעיון על הפרק (אשמח ל-Fork מי שמממש).

תהנו (בעתיד יתווסף EXE עם CLI)
