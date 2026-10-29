# NikoboiNFTB/DeSlop

⭐ 18 · JavaScript · GPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/NikoboiNFTB/DeSlop) · [官网](https://addons.mozilla.org/firefox/addon/youtube-deslop/) · 个人维护

**按黑名单过滤 YouTube 信息流中 AI 内容的浏览器扩展/脚本**

以用户脚本与浏览器扩展两种形式提供的内容过滤工具：从 GitHub 拉取频道黑名单，删除首页、订阅页中命中条目的视频，以及搜索结果中命中的视频与频道；黑名单覆盖完全 AI 生成内容的频道及教授 AI 内容制作的频道。用户可通过 PR、Issue 或邮件提交黑名单条目或申诉。提供 Firefox 附加组件安装、Chromium 本地加载未打包扩展与 Tampermonkey/Violentmonkey 用户脚本三种途径；README 声明不会上架 Chrome Web Store。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从 GitHub 拉取黑名单并匹配移除首页/订阅/搜索结果中的条目
- 同一功能覆盖 Firefox 附加组件、Chromium 本地扩展与用户脚本三种形式
- 社区通过 PR、Issue、邮件与即将上线的 Google Forms 提交黑名单条目
- 提供条目申诉（Entry Appeals）流程

## 适用场景

- 屏蔽 YouTube 信息流中完全 AI 生成的频道
- 从搜索结果中过滤 AI 内容频道
- 参与维护和扩充 AI 内容黑名单

## 场景标签

 · 领域:浏览器工具/内容过滤

## 证据(README 行号)

> L3: Userscript and browser extension for filtering out AI slop from your YouTube feed. Blocklist-driven.
> L9: Channels that publish fully AI-generated content as well as channels that promote or teach how to create it qualify 

## 星数曲线

```mermaid
xychart-beta
    title "NikoboiNFTB/DeSlop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 low · 依据 README sha `e3b43ffd2559` · [字段定义](../../DATASET.md)*
