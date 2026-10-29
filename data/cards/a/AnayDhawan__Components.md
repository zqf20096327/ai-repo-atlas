# AnayDhawan/Components

⭐ 18 · JavaScript · NOASSERTION · 推送 2026-10-03 · [GitHub](https://github.com/AnayDhawan/Components) · 个人维护

**让 AI 编码代理实时拉取成品 React/Tailwind 动效组件的技能**

一个面向 AI 编码代理（Claude Code、Codex、Cursor、Gemini）的 Claude Code 技能：本体为 SKILL.md 决策流程加 components.json 指针注册表，无自有可执行代码。代理根据用户描述匹配 39 个展示动效（来自 Aceternity、Magic UI、ReactBits、Cult UI、21st.dev 五个库），在构建时运行各库注册表命令实时拉取真实组件、安装依赖并适配品牌 token 与 reduced-motion；另含 12 个 shadcn 普通兜底组件。限制：需网络访问与 shadcn 初始化的 React+Tailwind 项目；Aceternity 组件本身不可再分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1 个技能收录 39 个实时拉取的展示动效与 12 个 shadcn 兜底组件
- 组件来自 Aceternity/Magic UI/ReactBits/Cult UI/21st.dev 五个库的官方注册表
- 策展指针而非静态拷贝，代码保持最新且上游许可证随行
- 提供 npx CLI 安装器，支持多代理（Claude Code/Codex/Cursor/Gemini）安装与更新校验

## 适用场景

- 让编码代理给落地页加上滚动 MacBook、WebGL 地球等动效而不手写代码
- 按品牌 token 与深色模式、响应式、reduced-motion 约束适配拉取的组件
- 普通界面元素（表单/表格/导航）走 shadcn/Tremor 兜底路径

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L44: `components` is a **sourcing** skill. It answers one question - *"which proven showpiece fits, and how do I make it
> L115: `components` is a Claude Code skill (markdown + a JSON registry - no executable code of its own).
> L146: The agent auto-discovers it from the `description` in `SKILL.md`. It needs **network access** at build time (to fe

## 星数曲线

```mermaid
xychart-beta
    title "AnayDhawan/Components 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1bf2635066e5` · [字段定义](../../DATASET.md)*
