# BCS1037/codian

⭐ 26 · TypeScript · AGPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/BCS1037/codian) · 个人维护 · 中文 README

**Obsidian 多本地编码 Agent 工作区插件**

Obsidian 插件，将笔记库与本地 CLI 编码 agent（claude/codex/kimi/grok/opencode/pi 共 6 种）接入同一工作区：侧边栏多标签对话、内联编辑实时 diff、CodeMirror 6 编辑器 @note/@folder 补全，统一管理 Skills、MCP 服务器、子 agent 与命令；认证、会话与权限沿用各 provider 原生机制，产物保存在笔记库内。Claude 支持自定义模型与多家 Anthropic 兼容端点（阿里百炼/火山方舟/DeepSeek 等），密钥存于 Obsidian SecretStorage。需 Obsidian 1.11.4+ 与已安装的 provider CLI。基于 Claudian（MIT）修改，衍生代码以 AGPL-3.0 授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 6 种本地 CLI 编码 agent，保留各 provider 原生认证/会话/权限边界
- 对话与推理结果、Skills、MCP 服务器统一在 vault 内管理
- 内联编辑带词级实时 diff 预览，支持 @note/@folder 补全与拖拽
- Claude 支持自定义模型与阿里百炼/火山方舟/DeepSeek 等 Anthropic 兼容端点

## 适用场景

- 在 Obsidian 中围绕笔记内容持续调用本地编码 agent
- 把笔记、文件夹与 agent 对话围绕同一问题组织管理
- 在国内兼容端点（百炼/火山方舟/DeepSeek）上使用 Claude 类模型

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: **Codian** is a multi-provider AI agent workspace for Obsidian. Instead of treating your vault as one-off context, 
> L18: - 🌐 **Provider-Native Connections**: Supports 6 local CLI providers (`claude`, `codex`, `kimi`, `grok`, `opencode`,

## 星数曲线

```mermaid
xychart-beta
    title "BCS1037/codian 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b78a56f6f61c` · [字段定义](../../DATASET.md)*
