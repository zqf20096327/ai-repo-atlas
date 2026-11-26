# wonseokjung/connect-ai-xr

⭐ 6 · HTML · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/wonseokjung/connect-ai-xr) · [官网](https://www.aicitybuilders.com/yahak/xr/) · 个人维护

**给编码 agent 安装技能，一句话生成可跑在 Meta Quest 上的 WebXR 应用**

CONNECT AI LAB 出品的一个 agent 技能包，通过 npx 安装到 Claude Code、Codex、Cursor 等编码 agent 中；用户口头描述需求，agent 自动选择模板（行星仪、展示间、AR 桌面、画廊等五个起始应用）、修改内容、运行检测（报错、性能、截图）并生成本地地址供 Meta Quest 浏览器打开。应用基于 three.js 以代码绘制，无图片或模型文件；生成结果自适应 Quest 3/3S（AR+VR）、Quest 2（VR）及普通电脑与手机浏览器。附带韩文免费教材（7 个提示词）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条 npx 命令将 WebXR 构建技能装入 Claude Code/Codex/Cursor 等 agent
- 五个代码绘制的起始应用（orrery/xr-room/product-showroom/ar-desk/gallery）
- agent 自动完成选择模板、修改、检测（错误/Quest 性能/截图）、生成 Quest 访问地址
- 生成结果跨设备自适应：Quest 3/3S AR+VR、Quest 2 VR、电脑与手机 3D

## 适用场景

- 给产品快速生成一个可绕行走看的 3D 展示间并在 Quest 打开
- 把照片做成可步入浏览的 3D 画廊
- 在 Quest 3/3S 上往真实桌面摆放可捏取的 AR 物件
- 把别处做的 3D 页面迁移到此流程在 Quest 上打开

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L8: **Say one sentence to your coding agent. Get an XR app that opens on Meta Quest, and in 3D on any computer or phone.
> L11: npx github:wonseokjung/connect-ai-xr install-skill
> L14: Paste that line into Claude Code, Codex, Antigravity or Cursor and ask it to install. Then say: "Make me an XR app 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `5df63ba9a364` · [字段定义](../../DATASET.md)*
