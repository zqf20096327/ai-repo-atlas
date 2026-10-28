# tomorinao-www/nonebot-plugin-anime-trace

⭐ 49 · Python · MIT · 推送 2025-11-07 · [GitHub](https://github.com/tomorinao-www/nonebot-plugin-anime-trace) · 个人维护 · 中文 README

**NoneBot2 插件：通过 ai.animedb.cn API 识别动漫/galgame 角色**

面向 NoneBot2 机器人框架的插件，封装 ai.animedb.cn 网站的角色识别 API：用户在聊天中发送图片（或回复/再发一张图片）并使用命令关键字（识别/角色/人物，可选 gal/动漫参数），插件调用远端 API 返回动漫或 galgame 角色识别结果。识别模型与推理均在远端网站完成，插件本身不运行模型；依赖该网站的可用性，README 常见问题列出网站后端超时等失败情形。支持通过 nb-cli 或 pip 安装，可在 .env 中配置命令符与是否合并转发消息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 ai.animedb.cn API 识别动漫与 galgame 角色
- 自定义命令符、命令关键字与合并转发消息配置
- 提供 nb-cli 与 pip 两种安装方式
- 已增加 AI 绘图鉴别功能

## 适用场景

- 在 QQ 群聊机器人中发图识别动漫角色
- 识别 galgame 角色并选择 gal 模型
- 鉴别图片是否为 AI 绘图

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: _✨ 通过 ai.animedb.cn 的 api 识别动漫、galgame 角色 ✨_
> L51: 命令: {#} {识别|角色|人物|} [gal|动漫]
> L57: 附带一张图片、或回复一张图片、或再发送一张图片

## 星数曲线

```mermaid
xychart-beta
    title "tomorinao-www/nonebot-plugin-anime-trace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-28 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b75569b2ca53` · [字段定义](../../DATASET.md)*
