# sheldon123z/Zotero-Notion-Paper-Flow

⭐ 77 · Python · NOASSERTION · 推送 2026-04-15 · [GitHub](https://github.com/sheldon123z/Zotero-Notion-Paper-Flow) · 个人维护 · 中文 README

**自动抓取 HuggingFace/arXiv 论文并 LLM 总结同步到 Notion/Zotero 的工具**

自动化论文收集管理工具：从 HuggingFace Daily Papers 与 arXiv 按关键词/分类抓取论文，下载 PDF，调用 LLM API（默认 Moonshot，可替换 DeepSeek 等）将摘要翻译为中文并解析动机、方法、结果，自动打标签，再通过 Notion、Zotero、Wolai、飞书 API 同步到对应平台，支持 Slack 通知与 crontab 定时调度。面向科研人员的文献追踪流程，需申请相应 LLM API key（KIMI_API_KEY 为必需），各同步平台 API 均为可选。以 PyPI 包（paper-flow）、源码及 Electron 桌面应用三种形式分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多数据源：HuggingFace Daily Papers 与 arXiv 关键词/分类搜索
- LLM 中文翻译摘要并解析动机、方法、结果与自动打标签
- 同步到 Notion、Zotero、Wolai、飞书，支持 Slack 通知与定时调度
- 提供 pip 安装与 Electron 桌面配置工具

## 适用场景

- 每天定时追踪指定领域的最新论文并自动入库 Zotero
- 让 LLM 把英文论文摘要翻成中文并同步到 Notion 页面
- 按关键词订阅 arXiv 分类论文并下载 PDF

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L8: 自动化论文收集和管理工具，从 HuggingFace Daily Papers 和 arXiv 获取论文，使用 LLM 服务进行中文翻译和分析，并同步到 Notion、Zotero 和 Wolai。
> L13: - 🤖 **LLM 智能分析**: 使用 Moonshot/DeepSeek 进行论文摘要翻译和分类
> L68: 本项目可以扫描HuggingFace的Daily Papers页面，解析页面，获取相关论文标题、截图、ID等，调用Arxiv库获取论文更完善的信息，调用LLM API（目前是调用的是Moonshot API）对摘要进行分析，首先翻

## 星数曲线

```mermaid
xychart-beta
    title "sheldon123z/Zotero-Notion-Paper-Flow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 75 --> 78
    line [76, 77, 77]
```

2026-10-18 76 → 2026-10-29 77（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8d17e1602df7` · [字段定义](../../DATASET.md)*
