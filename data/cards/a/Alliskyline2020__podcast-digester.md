# Alliskyline2020/podcast-digester

⭐ 10 · Python · MIT · 推送 2026-09-02 · [GitHub](https://github.com/Alliskyline2020/podcast-digester) · 个人维护 · 中文 README

**本地播客/视频蒸馏工具：贴链接生成转录、摘要与亮点**

本地单用户的播客/视频蒸馏应用：粘贴 YouTube/Bilibili/抖音/小宇宙链接或本地文件，经下载→转录→清洗→分章→摘要→亮点→洞察的多阶段流水线，产出 TL;DR 与值听裁定（Deep Listen/Skim/Skip）、逐章中文摘要、五类带时间戳引用的亮点、产品/技术/市场洞察，以及与播放器时间轴对齐的双语字幕。面向中文 PM、研究员、投资人等信息消费者。LLM 通过 openai_compatible/anthropic_compatible 两种 adapter 可插拔切换（DeepSeek/OpenAI/Claude/GLM/通义/豆包/Kimi），串行队列支持断点续跑与崩溃自愈。全局词库沉淀纠错结果。macOS 13+ 全功能（无字幕源需 Apple AFM 3 本地转录），Linux 仅支持自带字幕源，Windows 未测试；需 Python 3.11–3.13、Node.js 18+ 与 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 安装:github 包 `release-assets` 月下载无数据

## 能力要点

- 多阶段流水线（下载→转录→分章→摘要→亮点→洞察）带 JSON checkpoint 断点续跑
- 五类亮点（fact/insight/quote/contrarian/story）每条带原始字幕引用与时间戳，点击跳转播放
- 可插拔多 Provider LLM，设置页零代码配置或环境变量切换，不改代码
- 全局词库纠错：批量纠错、编辑器 difflib 自学习、新播客自动套用

## 适用场景

- 把长播客/视频蒸馏成 5 分钟可决策的摘要与亮点，决定是否深听
- 生成与播放器时间轴对齐的双语字幕，按章节/亮点跳着听
- 批量粘贴链接排队处理，导出 HTML 成果与音频库归档

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: 粘贴一个链接 → 自动排队、下载、转录、清洗、分章、摘要、提炼亮点 → 双语字幕点击即跳转播放。
> L21: 信息工作者面对一集 2 小时的播客，最大的成本不是「听不懂」，而是**「不知道值不值得听」**。Podcast Digester 把一集音频蒸馏成：
> L23: - 一句话 **TL;DR** + **值听裁定**（`Deep Listen` / `Skim` / `Skip` 三档，拿不准默认 `Skim`）

## 星数曲线

```mermaid
xychart-beta
    title "Alliskyline2020/podcast-digester 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-10-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `443c789eb8c0` · [字段定义](../../DATASET.md)*
