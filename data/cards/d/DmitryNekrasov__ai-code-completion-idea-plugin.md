# DmitryNekrasov/ai-code-completion-idea-plugin

⭐ 20 · Kotlin · MIT · 推送 2026-02-09 · [GitHub](https://github.com/DmitryNekrasov/ai-code-completion-idea-plugin) · 个人维护

**IntelliJ IDEA 行内代码补全插件，由本地 LLM 生成建议**

基于 IntelliJ 平台的代码补全插件：在光标处切分文档前缀/后缀，先查本地缓存，未命中则调用外部 AI 模型（经本地 Ollama 运行 codellama:7b-code）生成建议，以灰色行内文本呈现，并做单行格式调整、预取缓存与插入统计。安装需先部署 Ollama 服务并拉取模型，再从 Releases 下载插件 zip 在 IDEA 中从磁盘安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于光标前缀/后缀上下文的行内补全建议（灰色文本）
- 本地缓存命中优先，未命中才查询模型，并预取后续建议
- 配合本地 Ollama 运行 codellama:7b-code 模型
- 记录建议插入事件用于统计

## 适用场景

- 在 IntelliJ IDEA 中获得本地 LLM 驱动的行内代码补全
- 希望补全程式离线本地运行、不经云端服务的开发者
- 减少重复输入，提升编码连续性

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: Implementation of IntelliJ IDEA code completion plugin using a local LLM.
> L11: 3. **AI Model Query.** If no relevant suggestion is found in the cache (a cache miss), the plugin queries an extern

## 星数曲线

```mermaid
xychart-beta
    title "DmitryNekrasov/ai-code-completion-idea-plugin 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b52a5df29770` · [字段定义](../../DATASET.md)*
