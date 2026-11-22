# namchengwuqiu/bilibili_autopilot

⭐ 3 · Python · MIT · 推送 2026-11-19 · [GitHub](https://github.com/namchengwuqiu/bilibili_autopilot) · [官网](https://github.com/namchengwuqiu/bilibili_autopilot#readme) · 个人维护 · 中文 README

**让 MaiBot 机器人在 B 站自主浏览并生成评论的插件**

MaiBot 平台的第三方插件（local.bilibili-autopilot），登录 B 站账号后自动读取首页推荐，过滤广告、直播与屏蔽词，结合麦麦人设与兴趣判断是否浏览，读取 B 站 AI 摘要或字幕生成一级评论并跟进回复，可分享视频到 QQ 群。提供 WebUI 管理页、额度限制、SQLite 持久化与发送结果核对机制。需 MaiBot 1.3.10～1.4.7 与扫码登录；不做音频转写或画面分析，不点赞、不投币、不发弹幕。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于人设与兴趣的浏览意愿判断，模型可决定休息或浏览
- 读取 B 站 AI 摘要或字幕生成评论，内容依据复核后达兴趣阈值才发送
- SQLite 事务记录发送意图，未知结果需人工 ack 核对，不自动重试
- WebUI 管理页与聊天命令查询浏览、评论与跟进记录

## 适用场景

- 让 QQ 群里的麦麦机器人以账号身份在 B 站刷视频并参与评论
- 在管理页查看模型调用用量、评论额度与发送记录
- 评论后自动把视频卡片和感想分享到已加入的 QQ 群

## 场景标签

 · 领域:社交平台自动化/机器人插件

## 证据(README 行号)

> L7: 麦麦独立插件 `local.bilibili-autopilot`。登录你指定的账号后，默认自动进入自主模式：麦麦先结合人设、兴趣、时间和最近的浏览反馈决定这次刷不刷 B 站，再结合视频内容决定要不要发表评论。
> L13: - 优先读取 B 站 AI 摘要；没有摘要时读取字幕。准备评论时按主题补充字幕并复核正文。没有足够内容或为多 P 视频时跳过，不凭标题编造观后感。

## 星数曲线

```mermaid
xychart-beta
    title "namchengwuqiu/bilibili_autopilot 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-02 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e4e0d0bc60d9` · [字段定义](../../DATASET.md)*
