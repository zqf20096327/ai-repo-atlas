# momo2young/humanize-academic-writing

⭐ 26 · Python · MIT · 推送 2026-01-25 · [GitHub](https://github.com/momo2young/humanize-academic-writing) · 个人维护 · 中文 README

**面向社科学者的 AI 技能：将 AI 生成的学术文本改写为自然学术写作**

一个以 SKILL.md 为核心的 AI 技能包，安装到 Cursor 或 Claude Code 后，通过对话指令（如 /humanize-academic-writing）识别 AI 生成英文文本中的机械转场、抽象措辞等 6+ 种写作痕迹，并改写为自然的学术表达。另附两个本地 Python 脚本用于检测与文本质量分析，仅依赖标准库、无数据外传。目标用户为社会科学研究者与非英语母语者，文档含中英双语版本，并给出学术诚信使用边界声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 识别 6+ 种 AI 写作模式并改写为学术化表达
- 附带本地运行的两个脚本：ai_detector.py 与 text_analyzer.py，零第三方依赖
- 针对 5 个社会科学学科给出学科特定写作规范
- 1370+ 行改写原则与示例文档，中英双语

## 适用场景

- 把自己研究中 AI 起草的英文论文段落改得更自然
- 检测论文草稿中残留的 AI 写作痕迹
- 作为非英语母语者按学科规范调整学术表达

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L8: An AI skill for Cursor and Claude Code that transforms AI-generated academic text into natural, human-like scholarly
> L46: ### ✅ Transforms AI Writing Patterns
> L81: 1. **AI Pattern Detection** - Automatically identifies 6+ AI writing markers

## 星数曲线

```mermaid
xychart-beta
    title "momo2young/humanize-academic-writing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fd7805b1b97d` · [字段定义](../../DATASET.md)*
