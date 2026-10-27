# spardanviro/Godot_AI

⭐ 55 · C++ · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/spardanviro/Godot_AI) · 个人维护 · 中文 README

**为 Godot 4.7 编辑器提供内嵌 AI 助手的原生 C++ 模块**

原生 C++ Godot 模块（非 GDExtension、非 addon），需放入引擎源码树编译进编辑器，在右侧停靠栏注册 AI 面板。面向 Godot 开发者：多 LLM 提供商对话（Anthropic/OpenAI 兼容/Gemini/DeepSeek/GLM），节点与文件 @ 提及注入上下文，解析 AI 回复生成 GDScript 并以 EditorScript 在编辑器内执行（执行前有静态安全策略检查，作者声明非沙箱）。按消息内容决定回答/执行/出计划，无模式切换。按需注入 Godot API 文档与 395 条 gotchas，常驻系统提示约 11K-33K 字符。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提供商支持：Anthropic、OpenAI 兼容、Gemini、DeepSeek、GLM，可指向自定义端点
- AI 生成的 GDScript 包装为 EditorScript 在编辑器内执行，带静态安全策略与权限检查
- @ 提及场景节点/文件并展开为结构化上下文（文件内容上限 5 万字符）
- 按需注入 API 参考与 395 条 Godot gotchas，避免静态全量注入

## 适用场景

- 在 Godot 编辑器内通过对话生成与执行 GDScript、搭建场景
- 让 AI 修复错误、做性能分析与调试辅助
- 提及项目节点/文件让 AI 基于项目上下文回答问题

## 场景标签

`AI 助手` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: AI assistant support inside the Godot editor as a native `ai_assistant` module, compatible with **Godot 4.7+** (godo
> L7: This project adds a docked AI panel to the editor, supports multiple LLM providers, and can execute AI-generated edi
> L11: `ai_assistant` is a native C++ Godot module. It is not a GDExtension and not a regular addon distributed as project

## 星数曲线

```mermaid
xychart-beta
    title "spardanviro/Godot_AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 53 --> 56
    line [54, 55, 55]
```

2026-10-18 54 → 2026-10-27 55（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2ae577a22b2a` · [字段定义](../../DATASET.md)*
