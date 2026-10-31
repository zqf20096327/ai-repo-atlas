# jacob7choi-xyz/harmonyrestorer-v1

⭐ 16 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/jacob7choi-xyz/harmonyrestorer-v1) · [官网](https://harmonyrestorer.online/) · 个人维护

**音频降噪 Web 应用：上传含噪音频，返回干净音频**

全栈音频降噪服务：用户上传 WAV/MP3/FLAC 等 6 种格式（≤50 MB、≤10 分钟）的含噪音频，通过自训练的 1D Operational GAN（基于 Ince et al. 2022 的 OpGAN，从零实现）或 UVR-DeNoise 引擎生成降噪音频，输出固定为 16 kHz 单声道。后端 FastAPI，前端 React/TypeScript，Docker Compose 部署。附带从公有领域古典录音构建训练数据的数据集管线，以及 1,091 项测试。先前发布的基准结果因训练/评估数据泄漏已撤回，待重新评测；生成始终以 16 kHz 单声道渲染。

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

- 从零实现的 1D Operational GAN（OpGAN）降噪模型
- 可选 UVR-DeNoise 引擎，经 DENOISER_ENGINE 切换
- 上传解码经 ffmpeg 校验（魔数、格式、时长），UUID 文件存储与速率限制等安全机制
- 提供数据集构建管线（公有领域古典录音 + 合成噪声，146,200 训练对）

## 适用场景

- 上传含噪录音文件获得降噪版本
- 对比自训练 OpGAN 与 UVR-DeNoise 的降噪结果
- 从古典录音与合成噪声构建音频降噪训练数据

## 场景标签

 · 领域:音频处理/深度学习

## 证据(README 行号)

> L3: AI-powered audio denoising. Upload noisy audio, get clean audio back.
> L5: - **Model**: Custom-trained OpGAN (1D Operational GAN). UVR-DeNoise via audio-separator is also available, selected 

## 星数曲线

```mermaid
xychart-beta
    title "jacob7choi-xyz/harmonyrestorer-v1 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `052dbf8ac78d` · [字段定义](../../DATASET.md)*
