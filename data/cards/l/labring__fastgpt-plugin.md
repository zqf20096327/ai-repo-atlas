# labring/fastgpt-plugin

⭐ 48 · TypeScript · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/labring/fastgpt-plugin) · 组织维护 · 中文 README

**FastGPT 插件系统：模型预设、系统工具与扩展功能**

FastGPT 团队将原系统工具迁移至本仓库并在此开发新工具，目标是对 FastGPT 做模块化以提升可扩展性。扩展模块覆盖系统工具、应用模板、模型预设，规划中含 RAG 算法、Agent 策略与第三方集成。系统工具支持独立执行、热插拔、版本管理、SSE 流式响应、本地调试与 URL 安装 SSRF 防护。提供 CLI 脚手架创建工具插件，经 pnpm 构建打包为 .pkg 上传。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 系统工具独立执行、热插拔与插件版本管理
- SSE 流式响应与本地插件调试支持
- npx CLI 脚手架生成工具插件并打包为 .pkg
- URL 安装含 SSRF 防护

## 适用场景

- 为 FastGPT 平台开发自定义工具插件
- 通过插件扩展 FastGPT 的模型预设与应用模板
- 本地调试并打包上传插件到 FastGPT

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: The system tools previously utilized in FastGPT have been migrated to this repository, and future development of ne
> L12: Deeply **modularize** FastGPT to achieve maximum **extensibility**.

## 星数曲线

```mermaid
xychart-beta
    title "labring/fastgpt-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-28 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `dc2b0e50b040` · [字段定义](../../DATASET.md)*
