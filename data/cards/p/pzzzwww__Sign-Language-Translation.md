# pzzzwww/Sign-Language-Translation

⭐ 48 · Python · MIT · 推送 2026-07-24 · [GitHub](https://github.com/pzzzwww/Sign-Language-Translation) · 个人维护 · 中文 README

**面向听障用户的实时手语识别转中文语音系统**

端到端实时手语识别与语音合成平台：摄像头采集图像后经 MediaPipe 提取 21 点手部关键点，CSL Transformer（4 层 8 头）做时序分类识别 26 类手势词汇，Qwen2-0.5B 将词汇序列重组为中文语句，pyttsx3 离线合成语音。支持 WebSocket 实时推流（CPU 30fps+）与 REST 视频上传两种方式，内置多层降级（启发式规则、Mock 映射表、CPU 回退）与 ONNX int8 量化导出。预训练权重随仓库提供，克隆安装依赖即可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MediaPipe + CSL Transformer 实时识别 26 类手势，CPU 30fps+
- Qwen2-0.5B 词汇重组 + pyttsx3 离线 TTS，无需付费 API
- 多层降级容错：权重缺失/Qwen2 失败/无 GPU 均有回退方案
- 支持 ONNX int8 量化部署与自定义词汇表训练

## 适用场景

- 听障人士通过手语与不懂手语的人交流
- 上传手语视频批量识别并生成中文句子和语音
- 基于自有手势数据扩展词汇表训练模型

## 场景标签

`语音合成` `多模态` · 领域:内容生成

## 证据(README 行号)

> L18: 端到端实时手语识别与语音合成平台。用户通过摄像头比划手语，系统自动识别手势词汇、重组为自然中文语句、合成语音播放。纯视觉方案，无需数据手套等昂贵硬件，普通摄像头即可使用。
> L21: 摄像头 → MediaPipe 关键点提取 → CSL Transformer 时序分类 → Qwen2 连词成句 → pyttsx3 语音合成
> L35: - **实时识别** — WebSocket 帧推流，MediaPipe + CSL Transformer 逐帧分类，CPU 30fps+

## 星数曲线

```mermaid
xychart-beta
    title "pzzzwww/Sign-Language-Translation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-29 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7be9e382a961` · [字段定义](../../DATASET.md)*
