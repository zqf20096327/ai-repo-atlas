# HaD0Yun/CozyClay

⭐ 2,016 · JavaScript · AGPL-3.0 · 推送 2026-11-18 · [GitHub](https://github.com/HaD0Yun/CozyClay) · [官网](https://cozyclay.org) · 个人维护

**浏览器端开源预演软件：搭建场景、调度镜头后交给 AI 视频模型**

运行于浏览器标签页的开源 previs 工具：用图元搭景、放置绑骨角色或替身胶囊，通过自然语言让 agent 生成 motion spec 并由浏览器内确定性编译器烘焙动作，QA 检查碰撞、脚滑、接触等；时间线上排布镜头、绘制轨道，导出首尾帧、greybox 参考视频、深度/法线通道、prompt 与 OTIO 剪辑表，供 AI 视频模型生成画面。支持 Agent 面板（ChatGPT 登录或自有 key）、MCP 服务与 CLI 三种驱动方式。安装仅需 npx cozyclay 与 Node 22.19+、Chromium，无需 GPU/Python/模型下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3D 场景调度 + 确定性动作编译与 QA（碰撞、脚滑、接触检查）
- 导出关键帧包：首尾帧、greybox 视频、深度/法线通道、prompt、OTIO 剪辑表
- 三种 AI 驱动界面：studio 内 Agent 面板、MCP 服务器、cclay live CLI
- 无需 GPU/Python/模型下载，npx 一条命令启动

## 适用场景

- 在 3D 里先定走位与镜头，再让 AI 视频模型按调度生成画面，减少按次付费的试错
- 用 Claude/Cursor 等 MCP 客户端实时驱动场景编排
- 制作分镜板、动态分镜（animatic）与镜头参照素材

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L4:  Open source previs in a browser tab: block the set, move the cast, cut the camera, hand the shot to an AI video mod
> L30: CozyClay lets you make those decisions first, in 3D, where they are cheap to change. Then the video

## 星数曲线

```mermaid
xychart-beta
    title "HaD0Yun/CozyClay 星数(近 10 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19"]
    y-axis "stars" 1530 --> 2060
    line [1574, 1716, 1721, 1749, 1766, 1822, 1844, 1848, 1951, 2016]
```

2026-11-08 1,574 → 2026-11-19 2,016（+442）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-17 · 置信度 high · 依据 README sha `29040d0140cd` · [字段定义](../../DATASET.md)*
