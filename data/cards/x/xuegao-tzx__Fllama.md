# xuegao-tzx/Fllama

⭐ 37 · C++ · MIT · 推送 2026-10-16 · [GitHub](https://github.com/xuegao-tzx/Fllama) · [官网](https://pub.dev/packages/fcllama) · 个人维护 · 中文 README

**llama.cpp 的 Flutter/鸿蒙 绑定库：移动端本地跑 LLaMA 模型**

通过 platform channel 将 llama.cpp 封装为 Flutter 插件（pub 包 fcllama），并提供 OpenHarmonyOS/HarmonyOS 的 HLlama 包（ohpm 安装）。支持初始化模型上下文、设备端模型测速（bench）、tokenize/detokenize、流式 token 监听、停止与释放上下文等 API。支持 Android（min SDK 23，arm64-v8a/x86_64/armeabi-v7a）、iOS（min 14，支持 Metal，Apple7 GPU 为最低要求）、HarmonyOS（API 12）。Android 尚未集成 GPU 后端，iOS 模拟器不支持 Metal 路径。模型需自行从 HuggingFace 获取 GGUF 格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Flutter platform channel 绑定 llama.cpp，pub 包 fcllama
- 提供 initContext/bench/tokenize/onTokenStream/release 等 Dart API
- 覆盖 Android、iOS、OpenHarmonyOS/HarmonyOS 三端
- iOS 支持 Metal 加速（Apple7 GPU 最低要求）

## 适用场景

- Flutter 应用中集成本地 LLM 推理
- 鸿蒙应用内运行 GGUF 模型
- 在移动设备上对模型做推理性能测试

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: Flutter binding of llama.cpp , which use platform channel .
> L15: flutter pub add fcllama

## 星数曲线

```mermaid
xychart-beta
    title "xuegao-tzx/Fllama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `34a6afb833b9` · [字段定义](../../DATASET.md)*
