# Universal Engineering Skills Library (91 Skills)

এই Library-তে ৯১টি আলাদা Skill আছে। প্রতিটি Skill-এর নিজস্ব `.claude/skills/<skill-name>/SKILL.md` ফাইল রয়েছে। এটি Claude Code এবং OpenCode—দুটির জন্য একই skill source ব্যবহার করে।

## কী আছে

- ৬৩টি Universal Software & Engineering Skills
- ১০টি Android ও AI Application Specialized Skills
- তোমার দেওয়া ZIP থেকে ১৫টি Documentary Skills (মূল workflow নির্দেশনা সংরক্ষিত)
- Documentary production সম্পূর্ণ করার জন্য নতুন ৩টি Skill: `documentary-media-generator`, `ai-voice-generation-engineer`, `automated-video-renderer`

## ব্যবহার: project-local

1. ZIP extract করো।
2. যে project-এ Skills ব্যবহার করবে, তার root folder-এ এই archive-এর `.claude/skills/` folder কপি করো।
3. Claude Code বা OpenCode-এ project root open করো।
4. Skill list/discovery যাচাই করো। Claude Code-এ `/skill-name` এবং OpenCode-এ `@skill-name` দিয়ে উল্লেখ করতে পারো; agent automatic discovery-ও করতে পারে।

## ব্যবহার: global (Windows)

PowerShell খুলে extract করা folder-এ গিয়ে চালাও:

```powershell
.\install-global-windows.ps1
```

Script skills-গুলো `$HOME\.claude\skills`-এ copy করে। OpenCode-ও global Claude-compatible `~/.claude/skills/` path discover করে। Existing একই নামের Skill থাকলে overwrite না করে skip করবে।

## ব্যবহার: global (macOS/Linux)

```bash
chmod +x ./install-global-unix.sh
./install-global-unix.sh
```

এটিও `~/.claude/skills/`-এ কপি করে এবং existing folder overwrite করে না।

## যাচাই

Python 3 দিয়ে চালাও:

```bash
python scripts/validate_skills.py
```

Expected result: 91 skill folders validated.

## Documentary workflow

UNVELL DECODE-এর জন্য `@production-orchestrator` বা Claude Code-এ `/production-orchestrator` দিয়ে শুরু করো। এটি research → fact-check → Hindi script → storyboard → assets → voice/audio → subtitles → edit/render → QC → YouTube package ক্রম অনুসরণ করবে। Output ভাষা হবে Hindi (Devanagari); production workflow ব্যাখ্যা ব্যবহারকারীর পছন্দের ভাষায় হতে পারে।

গুরুত্বপূর্ণ: Skills নিজেরা AI image/video/voice generate করে না। সেজন্য বাস্তবে configured provider/tool, যথাযথ অনুমতি, এবং render tool দরকার। `router-integration-planner` আগে পরীক্ষা করবে কোন capability সত্যিই উপলব্ধ। API key কখনো SKILL.md, prompt, source code বা GitHub-এ রাখবে না।

## Overlap policy

কিছু Skills কাছাকাছি কাজ করে, কিন্তু তাদের দায়িত্ব আলাদা রাখা হয়েছে। উদাহরণ: `code-review-engineer` maintainability ও correctness দেখে; `secure-code-reviewer` security-specific defects দেখে। `audio-engineer` signal processing করে; `audio-designer` documentary soundscape পরিকল্পনা করে। `video-processing-engineer` file/stream transformations করে; `automated-video-renderer` approved timeline assemble ও final output verify করে।

## গুরুত্বপূর্ণ নিরাপত্তা ও অনুমোদন

- Reverse engineering শুধু নিজের বা অনুমোদিত software-এ।
- Provider limits, pricing, licenses, and feature support implementation-এর সময় current documentation থেকে verify করতে হবে।
- Paid generation, bulk jobs, deployment, upload, publication, and destructive changes-এর আগে user approval লাগবে।
- কোনো export/upload সফল হয়েছে বলা যাবে না যতক্ষণ actual file/status যাচাই হয়নি।
