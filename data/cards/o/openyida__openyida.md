# openyida/openyida

⭐ 234 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/openyida/openyida) · [官网](https://demo.aliwork.com/o/openyida/helpCenter) · 组织维护 · 中文 README

**连接 AI 编码工具与宜搭的 CLI，用对话构建低代码应用**

OpenYida 是连接 AI 编码代理与阿里宜搭（Yida）平台的命令行工具，npm 安装后提供 `openyida`/`yida` 命令，供 Codex、Claude Code、Cursor 等代理调用：创建应用与表单、生成并编译 React 自定义页面、配置审批流、查询表单/流程数据、管理 HTTP 连接器与诊断环境。登录采用钉钉 OAuth，支持宜搭与千问办公组织。产物为原生宜搭应用，可在宜搭平台继续编辑与部署；README 声明示例应用仅为视觉参考而非成品。

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

- 为 AI 编码代理提供稳定的 `openyida` CLI，覆盖应用/表单/页面/流程/连接器操作
- 支持 Fast 与 Plan 两种构建模式，Plan 模式先出可审阅方案再执行
- 支持 Codex、Claude Code、Cursor、千问办公等 9 种 AI 编码工具
- OAuth 令牌登录与多环境 auth profile 切换，内置环境诊断命令

## 适用场景

- 用自然语言在宜搭上创建 CRM、审批流等业务应用
- 让编码代理读取 PRD 与设计稿生成自定义页面并发布
- 批量导入导出宜搭应用、查询表单与流程数据
- 诊断宜搭环境与登录状态问题

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: **AI-native CLI for building applications with AI Yida.**
> L21: OpenYida is a bridge between AI coding tools and Yida. It gives agents a stable `openyida` CLI to create resources,
> L166: |Tool|Support|

## 星数曲线

```mermaid
xychart-beta
    title "openyida/openyida 星数(近 9 点)"
    x-axis ["2026-10-24", "2026-10-30", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-12", "2026-11-13", "2026-11-20", "2026-11-26"]
    y-axis "stars" 227 --> 235
    line [228, 229, 230, 228, 231, 232, 233, 234, 234]
```

2026-10-24 228 → 2026-11-26 234（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `c7b2110469c4` · [字段定义](../../DATASET.md)*
