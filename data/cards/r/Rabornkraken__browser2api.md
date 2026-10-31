# Rabornkraken/browser2api

⭐ 28 · Python · 推送 2026-03-02 · [GitHub](https://github.com/Rabornkraken/browser2api) · 个人维护 · 中文 README

**将即梦AI/Google Flow 网页 UI 自动化为图像视频生成 API**

通过 Playwright 与 Chrome CDP 自动化操作 Jimeng（即梦AI）与 Google Flow 的网页界面，把浏览器交互封装为可编程的图像与视频生成接口，无需平台 API key 或逆向。工作流程为：经 CDP 启动真实 Chrome、首次手动登录并持久化会话、UI 自动化填写 prompt 并提交、拦截网络响应与轮询 DOM 捕获结果后下载。支持 Seedream/Seedance/Imagen/Nano Banana/Veo 等模型系列。需本地安装 Chrome 与 Python 3.11+；即梦视频生成与 4K 需会员，部分地区 Google Flow 需 VPN，仅供个人/研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动化即梦AI（Seedream 图像 / Seedance 视频，最高4K/1080p）
- 自动化 Google Flow（Imagen 4 / Nano Banana 2 / Veo 3.1）
- 无需 API key 或逆向，基于真实 Chrome CDP 反检测
- 会话持久化于 ~/.browser2api/，支持命令行与 Python API 调用

## 适用场景

- 用脚本批量调用即梦AI或 Google Flow 生成图像与视频
- 在无官方 API 的情况下将网页生成工具接入自己的程序
- 通过 Python 异步客户端程序化控制生成参数（模型/比例/分辨率）

## 场景标签

`浏览器自动化` `图像生成` `视频生成` · 领域:效率与自动化

## 证据(README 行号)

> L3: Turn browser UIs into programmatic image and video generation APIs.
> L17: **Image**: Seedream 5.0 — up to 4 images, 2K/4K
> L18: **Video**: Seedance 2.0 — 5s/10s, up to 1080p

## 星数曲线

```mermaid
xychart-beta
    title "Rabornkraken/browser2api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bae7a0d7b4d2` · [字段定义](../../DATASET.md)*
