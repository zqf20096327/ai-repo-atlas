# Yashsomalkar/noisegate

⭐ 14 · Rust · NOASSERTION · 推送 2026-04-25 · [GitHub](https://github.com/Yashsomalkar/noisegate) · [官网](https://github.com/Yashsomalkar/noisegate) · 个人维护

**Windows 实时麦克风降噪工具：Rust 运行 RNNoise/ONNX 模型**

Windows 系统托盘应用，经 WASAPI 低延迟采集麦克风音频，用降噪模型处理后写入 VB-Cable 虚拟音频设备，使 Zoom/Teams/Discord/OBS 等应用获得降噪后的麦克风信号。默认后端为 RNNoise（nnnoiseless 纯 Rust 移植，模型内嵌），可选 ONNX 后端加载 DeepFilterNet3 等模型（需自备 onnxruntime.dll 与模型文件）。10ms 帧端到端、三个 MMCSS 优先级线程与无锁 SPSC 环形缓冲。当前为 pre-alpha 状态，尚无预编译发布，需自行编译；仅支持 Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 默认 RNNoise 纯 Rust 后端，模型内嵌、单静态二进制约 10MB
- 可选 ONNX 后端加载 DeepFilterNet3 等模型（--features onnx）
- WASAPI 低延迟 I/O + VB-Cable 路由，任意应用可选为麦克风
- 系统托盘 UI 与 config.toml 配置（输入设备、衰减量、自启动）

## 适用场景

- 视频会议与直播时给麦克风做实时降噪
- 在 CPU 上替代付费或需 GPU 的降噪软件
- 通过 VB-Cable 让浏览器/Discord 等应用使用降噪麦克风

## 场景标签

 · 领域:音频/语音增强

## 证据(README 行号)

> L9: Real-time microphone noise cancellation for Windows. Pure-Rust inference, WASAPI low-latency capture/render, system-
> L21: - **DSP model:** **RNNoise** by default (via the `nnnoiseless` crate — pure-Rust port). Optional **ONNX** path for 
> L41: |**RNNoise** (via `nnnoiseless`)|✅|★★★ Good. Excellent for stationary noise (fans, hum). Older classical-RNN archit

## 星数曲线

```mermaid
xychart-beta
    title "Yashsomalkar/noisegate 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b45abb988a31` · [字段定义](../../DATASET.md)*
