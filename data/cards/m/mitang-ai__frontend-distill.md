# mitang-ai/frontend-distill

⭐ 16 · JavaScript · MIT · 推送 2026-04-13 · [GitHub](https://github.com/mitang-ai/frontend-distill) · 个人维护 · 中文 README

**把真实网站蒸馏成 AI 可复用前端设计资料的 skill 工具链**

面向 Claude Code 类 agent 的前端蒸馏 skill 加工具链：用 Playwright 访问目标网站，自动采集视觉 token、组件样本、布局与响应式线索，经去重、聚类、归一化整理后输出 DESIGN.md、LAYOUT.md 及 design-tokens.json / layout-tokens.json 四类产物，供 agent 低成本读取复用。工作方式是脚本承担确定性采集，提示词只做编排，AI 最后消费结构化结果。声明边界：读取公开渲染结果而非设计源文件，交互态与多 viewport 采样覆盖有限。

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

- 四层产物：DESIGN.md / LAYOUT.md / design-tokens.json / layout-tokens.json
- Playwright 自动采集：截图、懒加载触发、raw extraction 与 bundle 生成
- bundle 标准化、校验、拆分工具链与结构化 schema
- skill 安装后生成 RUNTIME.md 供 agent 直接调用工具路径

## 适用场景

- 从参考网站提取可复用的设计规范与结构化 tokens
- 给 AI 前端生成任务提供低歧义的布局与响应式约束
- 把已有 raw extraction JSON 整理成 design/layout tokens

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L17: `Frontend Distill` 是一个开源的前端蒸馏.skill + 工具链，用来从真实网站提取视觉、布局和响应式信息，并整理成便于复用的文档与 tokens。
> L44: - 精准提示词驱动的 skill
> L179: 4. 交给 skill 消费

## 星数曲线

```mermaid
xychart-beta
    title "mitang-ai/frontend-distill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `26b9406c62b6` · [字段定义](../../DATASET.md)*
