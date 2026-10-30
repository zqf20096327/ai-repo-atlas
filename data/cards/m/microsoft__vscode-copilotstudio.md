# microsoft/vscode-copilotstudio

⭐ 115 · C# · MIT · 推送 2026-10-29 · [GitHub](https://github.com/microsoft/vscode-copilotstudio) · 组织维护

**VS Code 扩展：在本地编辑与同步 Copilot Studio 智能体**

微软官方的 Visual Studio Code 扩展，用于开发 Microsoft Copilot Studio 智能体。功能包括：登录 Copilot Studio 环境后列出并克隆智能体到本地文件夹（知识源、动作、主题、触发器等组件以 YAML 文件形式保存）、对 YAML 组件提供 IntelliSense 补全与提示、通过 Preview/Get/Apply 变更命令在本地工作区与云端智能体间双向同步（Apply 为实时更新）。代码仓库含 .NET 语言服务器（C#），E2E 测试需配置开发环境并安装 msagent CLI。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 克隆云端智能体到本地并以 YAML 文件编辑各组件
- 对智能体 YAML 提供 IntelliSense 补全与提示
- 本地工作区与 Copilot Studio 智能体的双向同步（实时更新）
- 内置带 Session ID 的问题报告命令

## 适用场景

- 在 VS Code 中用代码编辑方式维护 Copilot Studio 智能体
- 对智能体配置做本地版本化与变更预览
- 团队在本地编辑后一键同步到云端智能体

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Copilot Studio Extension for Visual Studio Code
> L3: The Copilot Studio extension for Visual Studio Code is designed to enhance the development experience of Microsoft C

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/vscode-copilotstudio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 114 --> 116
    line [115, 115]
```

2026-10-18 115 → 2026-10-30 115（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2aef50ff35ab` · [字段定义](../../DATASET.md)*
