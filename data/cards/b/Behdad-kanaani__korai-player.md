# Behdad-kanaani/korai-player

⭐ 16 · JavaScript · NOASSERTION · 推送 2026-10-17 · [GitHub](https://github.com/Behdad-kanaani/korai-player) · [官网](https://behdad-kanaani.github.io/kmp) · 个人维护

**本地优先的桌面音乐播放器，含 DSP、BPM 检测与离线推荐**

面向拥有本地音乐文件的用户，基于 Electron 的 Windows 桌面播放器：提供曲库管理（元数据、封面、CUE）、播放队列、播放列表（M3U/PLS/XSPF 等格式）、共享音频总线 KoraiAudioEngine 的 DSP 链与 11 个内置声音配置、Graphic Studio 均衡器与频谱可视化、BPM 检测（FFmpeg 解码 + onset 包络）、以及基于本地收听历史与曲库信号的推荐。核心播放无需账号或订阅，数据以本地为主；明确声明人声提取非 AI 模型。支持波斯语/英语界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- KoraiAudioEngine 共享音频总线：前置放大→低切→EQ→混响→压缩→限制器的完整 DSP 链
- 本地信号驱动的推荐：收听历史、喜欢/跳过、BPM、内容相似度
- FFmpeg 解码 + onset 包络的 BPM 检测，处理半速/倍速歧义
- 插件系统含 worker、权限处理、热重载与注册表目录

## 适用场景

- 管理和播放自己已有的本地音乐收藏
- 用声音配置和 DSP 调整适配耳机或音箱
- 在不依赖流媒体账号的情况下获得本地曲库推荐
- 为歌曲检测 BPM 并组织播放列表

## 场景标签

 · 领域:音频/桌面媒体播放

## 证据(README 行号)

> L9: KORAI is a desktop music player for building, organizing, and enjoying your own music library. It combines library m
> L144: The vocal extraction feature uses stereo center-channel processing. It is **not an AI source-separation model**, a
> L150: This approach is intended to provide useful suggestions without requiring a large remote AI service for core local

## 星数曲线

```mermaid
xychart-beta
    title "Behdad-kanaani/korai-player 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `115daa99757d` · [字段定义](../../DATASET.md)*
