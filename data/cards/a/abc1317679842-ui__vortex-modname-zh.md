# abc1317679842-ui/vortex-modname-zh

⭐ 3 · JavaScript · NOASSERTION · 推送 2026-11-15 · [GitHub](https://github.com/abc1317679842-ui/vortex-modname-zh) · [官网](https://www.nexusmods.com/site/mods/2475) · 个人维护 · 中文 README

**给 Vortex 模组管理器做全界面汉化与模组名 AI 翻译的扩展**

以 Vortex 扩展形式发布的中文本地化包：内置 6046+ 条界面词库与 759 条游戏固定译名，写入 i18next 最高优先级目录实现离线界面汉化；模组名、合集名、更新日志走 AI 翻译，通过 OpenAI 兼容接口调用本地 LM Studio/Ollama 或云端服务，带缓存落盘、路径占位符保护、长文分段机制。安装方式为 Releases 下载 zip 后在 Vortex 扩展页「从文件安装」，不填接口地址时仅启用界面词库部分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层机制：语言包接管、DOM 实时翻译、AI 长文本翻译
- 词库命中不联网，接本地模型可全程离线
- 译文缓存落盘 domCache.json/cache.json，重启不重翻
- 支持 LM Studio/Ollama 等任何 OpenAI 兼容接口

## 适用场景

- 把 Vortex 模组管理器界面变成中文
- 让词库里没有的模组名、合集名自动翻译成中文
- 翻译几千字符的模组更新日志
- 断网环境下用本地模型离线翻译

## 场景标签

 · 领域:游戏/桌面工具/本地化

## 证据(README 行号)

> L1: # Vortex 全界面汉化 + 模组名 AI 翻译
> L45: 市面上给 Vortex 汉化的做法基本就是塞一份 `common.json`。这个扩展分三层，各管一段：
> L51: |**AI 长文本**|模组名、合集名、更新日志、模组简介|任意 OpenAI 兼容接口：本地 LM Studio / Ollama，或云端|

## 星数曲线

```mermaid
xychart-beta
    title "abc1317679842-ui/vortex-modname-zh 星数(近 2 点)"
    x-axis ["2026-11-21", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-21 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `c32ada29ac5f` · [字段定义](../../DATASET.md)*
