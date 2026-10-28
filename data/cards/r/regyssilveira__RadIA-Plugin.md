# regyssilveira/RadIA-Plugin

⭐ 40 · Pascal · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/regyssilveira/RadIA-Plugin) · [官网](https://regys.com.br) · 个人维护

**Delphi IDE 的 AI 助手插件：聊天、代码生成与 IDE 工具代理**

基于 Embarcadero Open Tools API 的 Delphi IDE 插件，提供可停靠 VCL/WebView2 聊天窗、SSE 流式输出与视觉重构。功能覆盖代码生成与解释、Ghost Text/FIM 补全、项目/单元/Form 创建、编译与 DUnitX 测试、调试器与 Form Designer 控制、FastMM5 内存诊断、本地项目索引，以及带同意与检查点机制的代理模式（213 个工具目录）。支持 provider API/本地端点接入，也可将执行委托给外部 CLI（Codex/Claude/Gemini/Copilot），并通过 MCP 向授权客户端发布 IDE 工具。兼容 Delphi 12/13（Win32 与 IDE64），通过安装包或 PowerShell 脚本从源码构建；凭据以 Windows DPAPI 本地保护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 代理模式带同意、检查点与工具风险分级机制
- 213 个内部工具目录覆盖编辑器、编译、测试、调试器与 Designer
- 可委托外部 CLI（Codex/Claude/Gemini/Copilot）执行，也支持 MCP 发布 IDE 工具
- Ghost Text/FIM 内联补全与分块变更评审

## 适用场景

- 在 Delphi IDE 内通过对话生成、解释与重构代码
- 让代理创建项目、编译、跑测试并诊断失败
- 用 FireDAC Advisor 审计和现代化数据访问层
- 通过 MCP 把 IDE 工具暴露给本地授权客户端

## 场景标签

`AI 助手` `代码生成` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: O RadIA conecta chat, geração de código e um agente com ferramentas reais da IDE. Ele pode ler e
> L90: - **provider** conecta o chat a um modelo por API, endpoint local ou transporte declarado;

## 星数曲线

```mermaid
xychart-beta
    title "regyssilveira/RadIA-Plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-28 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3b37e743be77` · [字段定义](../../DATASET.md)*
