# system1970/opencode-mobile-use

⭐ 48 · TypeScript · MIT · 推送 2026-08-14 · [GitHub](https://github.com/system1970/opencode-mobile-use) · [官网](https://www.npmjs.com/package/opencode-mobile-use) · 个人维护

**OpenCode 插件：让 AI agent 通过 adb 遥控 Android 手机**

面向 OpenCode V2 的双端插件（server 端工具+技能，TUI 端侧栏投屏），通过 adb（USB/无线/Tailscale）连接 Android 手机，向 agent 注册 12 个 phone_* 工具（截图、UI 层级 dump、点击、滑动、输入、安装 APK、shell 等）与 7 个应用技能（WhatsApp/X/相机/Spotify/通话/GitHub 等），优先使用深度链接导航，并内置 phone-vision 视觉子代理兜底。仅支持 Android（需开启 USB 调试），无手机侧应用，依赖 OpenCode 特定 next 版本 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 12 个 phone_* 工具覆盖截图、UI dump、手势、输入、安装与 shell
- TUI 侧栏实时投屏（终端图像协议），支持 USB/无线/Tailscale 远程
- 带超时与媒体暂停策略的 resilient UI dump，适应不静止的界面
- 深度链接优先导航 + phone-vision 视觉子代理三级兜底

## 适用场景

- 在 OpenCode 中用自然语言指挥 agent 操作手机应用
- 远程（Tailscale）操控手机执行拍照、发消息、拨号等任务
- 为 agent 自动化 Android 设备测试与操作流程

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: - **12 agent tools** — `phone_devices`, `phone_screenshot` (SoM annotation + downscale), `phone_dump_ui`, `phone_ta
> L167: The server plugin registers the `phone_*` tools and skills through the OpenCode V2 plugin API. The TUI plugin rend
> L169: Everything talks to the phone over `adb` — over USB, wireless debugging, or a Tailscale tunnel. There is no phone-

## 星数曲线

```mermaid
xychart-beta
    title "system1970/opencode-mobile-use 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-30 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c70f0025b7f2` · [字段定义](../../DATASET.md)*
