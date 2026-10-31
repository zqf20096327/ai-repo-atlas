# DJH-001/multi-agent-job-search

⭐ 18 · Python · MIT · 推送 2026-08-02 · [GitHub](https://github.com/DJH-001/multi-agent-job-search) · [官网](https://github.com/DJH-001/multi-agent-job-search) · 个人维护 · 中文 README

**求职准备多 Agent 流水线：定轨选岗、定制简历、生成面试准备**

独立 Python 多 Agent 系统，通过 OpenAI 兼容 API 调用 LLM，包含 3 个 Agent（JD 分诊、简历定制、面试预测）与 5 道确定性护栏（G1-G5，3 阻断 2 提示），由编排器协调 5 套工作流并做状态双写（岗位级 JSON 与汇总 dashboard）。求职者可按保底/冲刺/边界三轨分级，护栏防止 AI 编造技能与数字；新技能需经 5 步人机协同晋升门方可写入材料。前身是 OpenCode 上的 SKILL.md 规则设计，现为纯 Python 独立运行（需 Python 3.9+ 与 API key，测试过 OpenAI 与 DeepSeek）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 3 个 Agent + 5 道护栏（含阻断式内容防火墙与真实数字校验）
- 保底/冲刺/边界三轨分诊与差异化治理策略
- 晋升门：新技能经 5 步人机确认后回流主简历
- 状态双写持久化与 44 个 pytest 测试

## 适用场景

- 我想根据 JD 和个人档案自动定制求职简历与面试准备
- 按匹配度把岗位分成保底/冲刺/边界分别准备
- 防止 AI 在简历和面试答案中编造未验证的技能或数字

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: A standalone Python multi-agent system for job search, featuring 3 AI agents, 5 safety guardrails, and workflow orch
> L15: - **3 agents** (triage, resume, interview) calling an LLM via the OpenAI-compatible API
> L35: 2. **TriageAgent** evaluates the JD against the candidate profile along three dimensions -- hard-skill match, hold-
> L37: 3. **ResumeAgent** extracts JD keywords, selects track-appropriate bullets from the master CV, and generates a tail

## 星数曲线

```mermaid
xychart-beta
    title "DJH-001/multi-agent-job-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `b6f31416f76e` · [字段定义](../../DATASET.md)*
