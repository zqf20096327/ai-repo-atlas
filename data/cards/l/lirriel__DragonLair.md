# lirriel/DragonLair

⭐ 3 · Swift · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/lirriel/DragonLair) · 个人维护

**为 iOS 用户把截图转为书籍/影视等书签的应用**

iOS 原生应用，将用户截取的屏幕截图识别为书签条目：调用用户自备 API key 的视觉模型解析截图内容，生成含标题、作者、年份、摘要与标签的书签，并按类别自动从 Apple Books、AniList、TMDB 等公开目录检索官方封面。支持应用内相册选取、Share Extension 分享、监视 Screenshots 相册三种导入方式，全部数据存储于本地 SwiftData，无后端与账号。构建需 Xcode 与 iOS 18 SDK，需自行配置签名文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种截图导入方式：应用内选取（单次最多 50 张）、Share Extension、监视 Screenshots 相册
- 支持 Claude、OpenAI、Gemini 三类 AI 供应商，用户自带 API key 与模型选择
- 七类内容分类，按类别从多个公开目录自动检索官方封面并做标题/年份校验
- 图像哈希与标题键两级去重，避免重复调用与重复建档

## 适用场景

- 把刷社交媒体时截下的书籍、漫画截图整理成书签清单
- 批量导入按日期区间的历史截图并自动清理相册
- 无服务器、本地保存的个人待读/待看记录管理

## 场景标签

`知识库管理` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L24: Dragon Lair is a personal hoard for those finds. It reads the screenshots for you. An AI vision model works out wha
> L42: - **Choose your AI:** Claude, OpenAI or Gemini, with your own model choice. Answers come back as strict JSON that m


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `1cdf3eac1dcf` · [字段定义](../../DATASET.md)*
