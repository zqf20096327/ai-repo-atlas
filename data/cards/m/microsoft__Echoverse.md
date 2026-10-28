# microsoft/Echoverse

⭐ 41 · HTML · MIT · 推送 2026-10-26 · [GitHub](https://github.com/microsoft/Echoverse) · 组织维护

**计算机使用 agent 的深度仿真环境工厂与评测 harness**

微软发布的 computer-use agent 环境子集：4 个环境（EchoStay 住宿市场、EchoForge 开发协作两个全领域世界，datepickers/nested_filter 两个能力世界，共 6 个任务切分、722 个任务）。每个环境为 FastAPI + Vite/React + SQLite 自包含应用，任务由数据库铸造答案、LLM judge（OpenAI/Azure OpenAI 兼容 API）判分。harness 负责启动环境、并发运行与验证结果，agent 由用户自带；可选 Fara1.5 参考 agent。grounding 数据库经 Hugging Face 数据集分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两类世界：全领域（保留共享线程/权限/审计等因果结构）与能力世界（单一控件跨布局，含 OOD 切分）
- 答案由环境真实数据库铸造，写任务对比 DB diff，成功判定基于应用状态而非截图
- harness agent 无关：可插拔 agent 接口（--agent），自带参考 agent Fara1.5
- LLM judge 支持 OpenAI、Azure OpenAI API key 与 Azure AD 凭据自动检测

## 适用场景

- 评测我的 computer-use agent 在真实状态网站任务上的表现
- 研究 agent 对未见布局的泛化（in-distribution vs OOD 对比）
- 并发跑多实例环境做规模化训练或测试

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L106: You bring your own agent — the harness only launches the environment and grades the outcome. See
> L28: serves a realistic web UI an agent can drive. Tasks are graded by an **LLM judge** over an

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Echoverse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ff8d78d30843` · [字段定义](../../DATASET.md)*
