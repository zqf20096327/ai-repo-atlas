# vual/ChatGPT-Next-Web-Pro

⭐ 802 · TypeScript · MIT · 推送 2026-07-19 · [GitHub](https://github.com/vual/ChatGPT-Next-Web-Pro) · 个人维护 · 中文 README

**面向终端用户的多模态 AI 聊天应用：绘图/音乐/视频/知识库问答及后台管理**

基于 ChatGPT-Next-Web 的增强分支，面向终端用户提供对话及多模态扩展：midjourney（含换脸/局部重绘的 plus 版）、Stable-Diffusion（sd-webui 接口）、Dall-E-3、gpt-image-1 绘图，suno 音乐、luma 视频，识图/whisper/tts，可将 fastgpt 知识库作为模型使用。提供无后台（开源）与有后台（登录注册、apikey/套餐/订单/会员管理、支付接入）两种形态，均通过 Docker 部署。有后台版本支持手机号/邮箱/公众号扫码登录及微信支付、易支付等国内支付方式。

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

- midjourney 标准版与 plus 版（AI 换脸、局部重绘）及独立绘图面板
- 接入 Stable-Diffusion（sd-webui 接口）、Dall-E-3、gpt-image-1
- fastgpt 知识库作为模型使用，解析 pdf/word/excel 等上传文件
- 有后台版本含登录注册、apikey/套餐/订单管理与微信支付/易支付/虎皮椒支付

## 适用场景

- 个人部署一个支持绘图、音乐、视频生成的多模态聊天站
- 搭建带登录注册和套餐售卖的 AI 服务站点
- 将 fastgpt 知识库接入聊天对话使用

## 场景标签

`聊天机器人` `图像生成` `视频生成` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: 基于 ChatGPT-Next-Web 的增强版本，覆盖多模态、绘图、音乐、视频等扩展，提供「无后台」与「有后台」两种形态。
> L46: |音乐|suno（chat 格式）|✓|✓|✓|
> L48: |多模态|识图、whisper、tts|✓|✓|✓|
> L50: |fastgpt|将 fastgpt 知识库作为模型使用|✓|✓|✓|

## 星数曲线

```mermaid
xychart-beta
    title "vual/ChatGPT-Next-Web-Pro 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-25"]
    y-axis "stars" 800 --> 803
    line [802, 801, 802, 802]
```

2026-10-18 802 → 2026-10-25 802（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0ac007d1949f` · [字段定义](../../DATASET.md)*
