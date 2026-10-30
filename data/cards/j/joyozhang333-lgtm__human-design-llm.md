# joyozhang333-lgtm/human-design-llm

⭐ 15 · Python · MIT · 推送 2026-08-29 · [GitHub](https://github.com/joyozhang333-lgtm/human-design-llm) · [官网](https://humandesign.guichu.chat) · 组织维护 · 中文 README

**开源人类图 AI：排盘、BodyGraph、全盘解读与 Agent Skill**

人类图（Human Design）开源产品与工具包：输入出生信息生成结构化 HumanDesignChart JSON，渲染固定模板 BodyGraph SVG，提供类型、权威、通道、天赋、职业、关系等多层中文解读，DeepSeek/Claude 驱动基于盘面事实的继续对话并带本地安全回退。可作 FastAPI+React Web 应用自托管、Python 库/CLI 使用，也可作为经审计的 Agent Skill 安装到 Codex、Claude Code、DeepSeek Harness、Hugging Face/OpenClaw、腾讯 WorkBuddy 六类宿主。仓库明确声明人类图定位为自我观察框架、不做科学准确率与命运承诺。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结构化排盘输出 HumanDesignChart JSON 并渲染 BodyGraph SVG
- L1-L3 多层中文主线阅读（定位/全盘叙事/细读）与 LLM 产品包
- 一份 Skill 包可安装到六类 Agent 宿主（Codex/Claude Code/DeepSeek Harness 等）
- 防编造校验、术语回归与盲测等评估基础设施

## 适用场景

- 免费自托管一套完整的人类图解读 Web 产品
- 在自己的 AI agent 中调用结构化排盘与解读能力
- 用 Python 库/CLI 批量排盘或生成报告

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L13: **Human Design LLM** 是 HumanDesign.guichu.chat 的完整开源代码。它既是一个可直接使用和自托管的人类图 Web 产品，也是一个可安装到 **Codex、Claude Code、DeepS
> L47: - **一轮只谈一件事**：DeepSeek 每轮给出一个具体判断、少量短段落和一个追问，通过用户的真实经历逐步校准，而不是一次倾倒标准答案。
> L58: |人类图排盘|输入出生日期、准确时间和出生地，生成稳定的 `HumanDesignChart` JSON|

## 星数曲线

```mermaid
xychart-beta
    title "joyozhang333-lgtm/human-design-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f8a707e6953b` · [字段定义](../../DATASET.md)*
