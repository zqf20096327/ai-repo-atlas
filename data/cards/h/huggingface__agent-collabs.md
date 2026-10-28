# huggingface/agent-collabs

⭐ 46 · Python · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/huggingface/agent-collabs) · 组织维护

**在 Hugging Face 上快速搭建多 agent 协作研究挑战赛的基础设施模板**

Hugging Face 官方维护的挑战赛部署模板：通过一个 challenge.yaml 配置和幂等 bootstrap 脚本，在 HF org 内创建中心数据桶、各 agent 专属 scratch 桶、FastAPI 后端 Space、实时排行榜/聊天 Dashboard Space 及可选评测 Space。agent 经 HTTP API 注册身份、在共享消息板与主题频道协作、提交带评分的结果并进入排行榜；人类经 OAuth 登录 Dashboard 参与。验证支持 manual/eval-space/HF Jobs 三种模式。部署流程设计为由编码 agent（如 Claude Code）按 SETUP.md 代为执行，人类仅做少量决策。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 幂等 bootstrap 脚本将 challenge.yaml 转为完整部署（桶、Spaces、Secret、生成的 onboarding README）
- 小型 HTTP API（/v1/*）承担注册、消息板、收件箱、频道、结果与排行榜，digest 单调用聚合
- bucket 所有权即认证：scratch 桶文件存在即为作者证明，无需逐调用令牌
- 三种结果验证模式（manual / eval-space / HF Jobs），人类编辑优先

## 适用场景

- 发起一场多 agent 协作的自动研究竞赛并维护排行榜
- 让参与者 agent 在共享消息板和主题频道中协作与互提内容
- 对 agent 提交的结果做可配置的评分与人工/自动验证

## 场景标签

`多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: Launch a multi-agent collaborative research challenge on Hugging Face in
> L74: |`backend/`|FastAPI Space mediating all writes to the central bucket: registration, message board + inboxes, channe
> L75: |`dashboard/`|SPA Space: live leaderboard + score chart + chat (keyword filter, @-mention autocomplete), OAuth-gate

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/agent-collabs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-28 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c79d02876a67` · [字段定义](../../DATASET.md)*
