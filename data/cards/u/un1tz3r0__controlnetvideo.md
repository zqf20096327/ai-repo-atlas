# un1tz3r0/controlnetvideo

⭐ 83 · Python · 推送 2026-06-09 · [GitHub](https://github.com/un1tz3r0/controlnetvideo) · 个人维护

**命令行工具：用 Stable Diffusion 重绘视频并保持帧间一致**

基于 Hugging Face diffusers 的 Python 命令行工具，对输入视频逐帧做 img2img 重绘，通过稠密光流做运动迁移并以前一帧输出作为反馈（ControlNet 或 IP-Adapter/reference-only 注入）来处理帧间一致性问题。支持 SDXL ControlNet-Union、Flux.1 canny、RAFT 等多种运动估计、六段可插拔视频滤镜链，以及基于 madmom 的音乐节拍同步参数动画（结果缓存为 .jsonl）。作者注明该脚本为实验性探索路径。安装方式为 git clone 源码加 pip 安装依赖，需在 venv 中运行 Python 脚本。

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

- 光流运动迁移 + 前帧反馈解决帧间一致性
- SDXL ControlNet-Union 单模型支持 depth/canny/openpose/softedge/normal
- 六段可插拔动画视频滤镜链（videofilters.py 亦可独立 CLI 使用）
- madmom 节拍分析与分段贝塞尔曲线参数调制

## 适用场景

- 用 SDXL/Flux 提示词重绘实拍视频
- 制作节拍同步参数变化的音乐视频
- 在扩散管线多个阶段叠加滤镜效果

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L4: This python script is a command line tool for rerendering videos with stable diffusion
> L6: It attempts to solve the problem of frame-to-frame consistency by various methods, primarily
> L8: controlnets or reference only attention coupling.

## 星数曲线

```mermaid
xychart-beta
    title "un1tz3r0/controlnetvideo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 82 --> 85
    line [84, 83, 83]
```

2026-10-18 84 → 2026-10-25 83（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `38fa07ae0499` · [字段定义](../../DATASET.md)*
