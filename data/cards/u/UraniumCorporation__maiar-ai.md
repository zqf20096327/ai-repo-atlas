# UraniumCorporation/maiar-ai

⭐ 87 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/UraniumCorporation/maiar-ai) · [官网](https://maiar.dev) · 组织维护

**插件式可组合 AI Agent 框架，供开发者构建智能体应用**

Node.js/TypeScript 的 AI Agent 框架，将智能体抽象为数据摄取触发、决策、动作执行三步，以插件形式定义触发器与动作，核心运行时通过模型辅助推理动态组装执行管道。架构借鉴 Unix 管道，插件沿结构化上下文链依次运行。默认配置使用 OpenAI 模型与 SQLite 对话记忆，也支持本地模型与自定义集成；数据库、模型提供方与日志均可替换。通过 pnpm create maiar 初始化项目，插件经 pnpm add 安装并加入运行时配置。仓库为 monorepo，含 starter 参考实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 触发器与动作以独立插件形式声明，运行时动态组装执行管道
- Unix 管道式上下文链，插件接收输入、执行操作、输出结构化结果
- 对数据库适配器、模型提供方（OpenAI/本地模型/自定义）、日志均不强绑定
- 提供 @maiar-ai/plugin-discord 等插件与 pnpm create maiar CLI 初始化

## 适用场景

- 构建触发-决策-执行模式的 AI Agent 应用
- 通过编写插件扩展智能体的触发与动作能力
- 接入 Discord 等平台运行对话型智能体

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: Instead of rigid workflows or monolithic agent logic, Maiar abstracts these steps into a **modular, plugin-based sy
> L161: At its core, MAIAR builds execution pipelines dynamically. When an event or request is received, the runtime:

## 星数曲线

```mermaid
xychart-beta
    title "UraniumCorporation/maiar-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-25 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `849d57732b19` · [字段定义](../../DATASET.md)*
