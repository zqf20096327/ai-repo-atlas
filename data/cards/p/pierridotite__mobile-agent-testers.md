# pierridotite/mobile-agent-testers

⭐ 45 · Python · MIT · 推送 2026-11-19 · [GitHub](https://github.com/pierridotite/mobile-agent-testers) · 个人维护 · 中文 README

**在 GitHub Actions 上用 20 个 Claude Code 代理并行众测移动应用 UI**

通过 GitHub Actions 工作流为每个测试角色（persona）分配独立的 iOS 模拟器或 Android 模拟器，每个模拟器上运行一个 Claude Code 代理，按设备型号、语言、字号、深色模式等设定探索应用并生成带截图的 bug 报告；结束后由 Claude 在本机将重复报告分组汇总。支持 Flutter、React Native、Expo、原生 Kotlin/Swift、KMP、Capacitor、.NET MAUI 及自定义构建命令，报告加密后离开 runner。运行结果每次探索路径不同，需人工核对截图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个 persona 独占一台模拟器/仿真器，最多约 20 个并行
- 每屏执行无障碍检查（未命名控件、小于 48dp/44pt 的触控目标）
- 报告、截图与录像在 runner 上加密，本机解密后自动去重汇总
- 可从 release APK 直接测试，无需本地构建

## 适用场景

- 发布前让多设备多语言角色探索式找 bug
- 检查大字号、深色模式、RTL 布局等无障碍问题
- 公开仓库零 runner 费用跑批量移动端测试

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: No test scripts to write. Each tester is a Claude Code agent with its own iOS
> L145:  How it works: one workflow builds the app, then one emulator or simulator with one agent per persona, encrypted r


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `b73ab9676c38` · [字段定义](../../DATASET.md)*
