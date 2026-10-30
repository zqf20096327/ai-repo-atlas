# Picovoice/falcon

⭐ 79 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/Picovoice/falcon) · 组织维护

**端侧说话人分离引擎：本地识别音频中不同说话人及其时段**

Picovoice 出品的设备端说话人分离（diarization）引擎，将音频切分并标注各说话人的发言时段，语音处理全程本地运行。跨平台提供 SDK：Python（pip）、C、Web（npm/yarn）、iOS（CocoaPods）、Android（Maven Central），覆盖 Linux/macOS/Windows、树莓派与移动/浏览器。使用需从 Picovoice Console 获取 AccessKey，且需联网向 Picovoice 许可服务器验证 AccessKey，账户有用量限制，超出需联系企业销售。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 说话人分离：识别音频中不同说话人及各自发言区间
- 全部语音处理本地运行，不上传音频
- 跨平台 SDK：Python/C/Web/iOS/Android，支持树莓派 3/4/5
- v2.0.0 支持在 GPU 或多 CPU 核心上运行

## 适用场景

- 给会议或访谈录音做多人发言时段标注
- 作为语音识别前置步骤区分说话人
- 在无网络上传要求的隐私场景中本地处理音频

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L16: Falcon is an on-device speaker diarization engine. Falcon is:
> L29: Speaker diarization, a fundamental step in automatic speech recognition and audio processing, focuses on identifyin

## 星数曲线

```mermaid
xychart-beta
    title "Picovoice/falcon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-30 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9beeec23a0a3` · [字段定义](../../DATASET.md)*
