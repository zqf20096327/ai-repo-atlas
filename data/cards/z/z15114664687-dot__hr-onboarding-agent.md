# z15114664687-dot/hr-onboarding-agent

⭐ 101 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/z15114664687-dot/hr-onboarding-agent) · 个人维护 · 中文 README

**Feishu/Lark 人力入职管理应用：AI 辅助文档提取与人工审核**

基于 FastAPI + SQLite 的人力入职流程应用：用 YAML 定义工作流节点、负责人与截止日期，候选人上传的材料经 OCR 提取后作为不可信数据处理，涉及后果的决定由确定性规则和人工审核控制；支持与飞书/Lark 回调、卡片及 Bitable 同步，并用 APScheduler 生成逾期提醒。模型层可插拔 Mock、OpenAI、Gemini、Ark/Doubao、Zhipu、DeepSeek，外部 AI 默认禁用。提供零凭据本地演示脚本与 Docker 方式。定位为早期参考实现，演示模式禁止处理真实 HR 数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- YAML 工作流引擎：安全加载、严格键校验、启动时 fail-closed
- 上传与 OCR 文本视为不可信数据，可疑指令强制人工审核
- Mock/OpenAI/Gemini/Ark(Doubao)/Zhipu/DeepSeek 可插拔 provider，外部 AI 需显式开启
- 零凭据本地演示：三名虚拟候选人、无飞书账号/模型 key 即可运行

## 适用场景

- 在飞书/Lark 环境中管理候选人从材料提交到 HR 审核的入职流程
- 试用带人工审核闸门的文档 OCR 与 AI 辅助提取工作流
- 作为带威胁模型与安全审计文档的入职系统参考实现进行二次开发

## 场景标签

`工作流自动化` `文档解析` · 领域:效率与自动化

## 证据(README 行号)

> L13: HR Onboarding Agent coordinates the journey from pre-boarding documents to HR review, reminders, and Feishu/Lark up
> L18: - Plug in mock, OpenAI, Gemini, Ark/Doubao, Zhipu, or DeepSeek paths.

## 星数曲线

```mermaid
xychart-beta
    title "z15114664687-dot/hr-onboarding-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-27 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `722156d76ce2` · [字段定义](../../DATASET.md)*
