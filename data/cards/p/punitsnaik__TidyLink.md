# punitsnaik/TidyLink

⭐ 23 · Kotlin · MIT · 推送 2026-10-26 · [GitHub](https://github.com/punitsnaik/TidyLink) · 个人维护

**Android 书签管理器：AI 自动分类与摘要保存的链接**

原生 Android 应用，通过系统分享菜单捕获任意应用中的 URL，后台抓取标题、描述与缩略图，并可调用用户自备 API key 的 LLM（任意 OpenAI 兼容端点，内置 Gemini/xAI Grok 预设）为链接生成分类与一句话摘要。数据全部留在设备端，无后端、无分析；提供浏览器书签 HTML 导入、去重归一化、SQLite FTS4 全文搜索、回收站与 JSON 备份。AI 功能为可选，未配置时链接保持未分类。需 Android 10+，通过 Releases 页 APK 或源码自行构建安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分享即保存，后台抓取元数据并 AI 分类摘要
- 支持任意 OpenAI 兼容端点，多 provider 限流自动轮换，密钥 Android Keystore 加密存储
- URL 规范化去重与 SQLite FTS4 前缀全文搜索
- 无后端无分析，库内数据仅设备端存储

## 适用场景

- 把聊天和浏览器里堆积的链接集中成可搜索的资料库
- 导入 Chrome/Firefox/Safari 书签并自动归类
- 给 YouTube/文章等链接打分类和一句话摘要方便回顾

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L7: A native Android app that captures URLs shared from any app, scrapes their metadata, and uses AI to automatically ca
> L27: **Everything stays on your device.** There is no backend and no analytics. AI categorization is optional and uses *
> L104: Without a provider configured, nothing is ever sent anywhere and links simply stay "Uncategorized".

## 星数曲线

```mermaid
xychart-beta
    title "punitsnaik/TidyLink 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fdfffe7c6da2` · [字段定义](../../DATASET.md)*
