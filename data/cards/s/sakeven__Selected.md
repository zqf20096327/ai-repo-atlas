# sakeven/Selected

⭐ 116 · Swift · GPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/sakeven/Selected) · [官网](https://plus.anynotes.app/) · 个人维护 · 中文 README

**macOS 划词操作菜单栏工具：搜索/翻译/朗读/AI 处理选中文本**

macOS 菜单栏应用，针对选中文本弹出操作栏：搜索、翻译、复制、朗读、打开链接、地图、计算器等；另提供 ⌥X 快速输入面板与默认关闭的剪贴板历史。AI 功能（翻译、聊天、摘要/润色/提取等）需配置 OpenAI 或 Claude API key，无 key 时搜索与复制仍可用。支持浏览器自动化读取网页选中文本与来源 URL，并通过 .selectedext 插件（config.yaml）自定义 URL、快捷键、AI Prompt、本地命令等动作。要求 macOS 15.0+，从 Releases 下载安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 选中文本弹出操作栏：搜索/翻译/复制/朗读/链接/地图/计算
- OpenAI 与 Claude 双 provider 配置，支持自定义 API Host 与模型
- 剪贴词历史（默认关闭）+ AI 动作（摘要/解释/润色/提取/翻译）
- 插件系统：可视化编辑器 + YAML，支持 URL/macOS Service/AI Prompt/本地命令动作

## 适用场景

- 在任何应用里划词后直接搜索、翻译或让 AI 摘要改写
- 通过快速输入面板处理未选中的文本
- 管理和复用剪贴板历史内容
- 自定义插件扩展文本处理动作

## 场景标签

`AI 助手` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L3: A macOS menu bar app for working with selected text. Select a passage to search, translate, copy, read aloud, or run
> L19: 5. Select text in another app and click an action on the toolbar. Search and copy work without an AI key. To use tr
> L59: Open **Settings → General** and choose **OpenAI** or **Claude** as the **AI Service**. Enter the key for that provi

## 星数曲线

```mermaid
xychart-beta
    title "sakeven/Selected 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 114 --> 117
    line [115, 116, 116]
```

2026-10-18 115 → 2026-10-26 116（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `48585ed928f2` · [字段定义](../../DATASET.md)*
