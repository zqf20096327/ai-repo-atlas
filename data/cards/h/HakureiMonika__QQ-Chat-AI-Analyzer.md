# HakureiMonika/QQ-Chat-AI-Analyzer

⭐ 44 · Python · GPL-3.0 · 推送 2026-01-12 · [GitHub](https://github.com/HakureiMonika/QQ-Chat-AI-Analyzer) · 个人维护 · 中文 README

**本地部署的 QQ 群聊记录 LLM 分析与年度报告生成工具**

基于开源项目 qq-chat-exporter 搭建的本地部署工具：读取 qce 导出的 JSON 格式 QQ 群聊记录，调用用户自行配置的 LLM API（URL/key/模型名）进行总结分析，生成 HTML 报告（含年度报告、动漫小剧场等），并提供报告历史记录与本地缓存下载。推荐聊天记录文件在 120MB 以下，超出建议手动裁剪；仅适配 qce 导出的 JSON 格式。作者声明工具由 Gemini-3-pro-preview 生成，出于学习科研目的。注意调用时聊天记录会完整上传至模型服务商。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Map/Reduce 式流程，可按模型上下文长度手动设置 Token 预算
- 支持配置多个模型服务商，单次分析可自由选择模型
- 动漫小剧场主题与最终输出增强（LLM 修复 HTML/CSS 美化）
- 报告历史记录本地缓存并提供下载

## 适用场景

- 为自己的 QQ 群生成年度总结报告
- 对导出的群聊 JSON 记录做 LLM 总结分析
- 生成带角色小剧场等定制化内容的群聊报告

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L2: 这是依赖于Github上的开源项目qq-chat-exporter-master搭建的本地部署的轻量化QQ群聊消息分析工具，出于学习科研目的而开发，可用于生成年度报告等有意思的分析报告。

## 星数曲线

```mermaid
xychart-beta
    title "HakureiMonika/QQ-Chat-AI-Analyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bd33494b0991` · [字段定义](../../DATASET.md)*
