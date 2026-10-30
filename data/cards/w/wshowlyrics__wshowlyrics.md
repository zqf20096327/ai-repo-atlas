# wshowlyrics/wshowlyrics

⭐ 15 · C · GPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/wshowlyrics/wshowlyrics) · [官网](https://wshowlyrics.github.io/wshowlyrics/) · 个人维护

**Linux 桌面歌词悬浮层：随播放同步显示与翻译歌词**

基于 Wayland (wlr-layer-shell) 的桌面歌词悬浮程序，构建于 wshowkeys。通过 playerctl 检测 MPRIS 兼容播放器的当前曲目，本地 LRC 文件优先、在线 lrclib.net 兜底获取歌词，支持 LRC/LRCX/SRT/VTT 格式、逐字卡拉OK填充效果、系统托盘专辑封面（iTunes API 兜底）与 D-Bus 实时调节时序偏移。翻译功能可选接入 OpenAI、DeepL、Gemini、Claude API 并带缓存。提供 AUR/PPA/COPR/NUR 及源码编译安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MPRIS 集成自动检测播放曲目并同步显示歌词
- 多翻译提供商（OpenAI/DeepL/Gemini/Claude）的歌词翻译与缓存
- LRCX 逐字级卡拉OK渐进填充效果
- D-Bus 实时调节歌词时序偏移与显示开关，支持 Sway/Hyprland 快捷键

## 适用场景

- 在 Wayland 桌面上边听歌边看同步歌词
- 把外语歌词自动翻译成目标语言对照显示
- 卡拉OK式逐字高亮跟唱

## 场景标签

 · 领域:桌面多媒体工具

## 证据(README 行号)

> L16: A Wayland-based lyrics overlay program. Built on wshowkeys by Drew DeVault (via this fork) and inspired by LyricsX.
> L38: - **Translation Support**: Multi-provider API integration for automatic lyrics translation
> L39:  - Multiple translation providers: OpenAI, DeepL, Google Gemini, Anthropic Claude

## 星数曲线

```mermaid
xychart-beta
    title "wshowlyrics/wshowlyrics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e6ab2a29780f` · [字段定义](../../DATASET.md)*
