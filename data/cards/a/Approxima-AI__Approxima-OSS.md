# Approxima-AI/Approxima-OSS

⭐ 35 · TypeScript · MIT · 推送 2026-06-12 · [GitHub](https://github.com/Approxima-AI/Approxima-OSS) · 组织维护

**开源 AI Agent 网页端到端测试平台，英文描述即可执行**

开源的 agent 驱动 Web E2E 测试平台：用英文编写测试步骤或仅给出目标，LLM 浏览器 agent（Playwright + LLM 循环）在真实浏览器中逐步执行、截图并视觉验证每一步。提供目标模式自动探索生成步骤、自愈式步骤修正、可复用 Skills、变量与加密密钥、agent 版本影子对比等功能。架构为 Next.js 面板 + Hono API（Cloudflare Workers）+ Node web-runner，运行需 Node 20+、Postgres、S3 兼容存储及至少一个 LLM API key。测试密钥会进入发送给云端模型的提示词，README 明示不应使用重要凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 英文步骤/目标驱动的 LLM 浏览器 agent，逐步截图视觉验证
- Goal 模式自动探索生成步骤并触发复现验证，此后确定性执行
- 自愈式步骤建议（LLM 复核后一键采纳）与可复用 Skills
- 秘密变量 AES-256-GCM 加密存储、界面掩码、日志脱敏

## 适用场景

- 用自然语言步骤替代选择器维护的 E2E 测试
- 仅给目标让 agent 自动探索并固化测试步骤
- 自托管测试套件并按计划定时运行

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L13: Approxima is an open-source, agent-based platform for end-to-end testing web applications. Write test journeys in E
> L77: |`web-runner/`|Node service that runs the browser agent (Playwright + LLM loop)|

## 星数曲线

```mermaid
xychart-beta
    title "Approxima-AI/Approxima-OSS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-26 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `54411d22358d` · [字段定义](../../DATASET.md)*
