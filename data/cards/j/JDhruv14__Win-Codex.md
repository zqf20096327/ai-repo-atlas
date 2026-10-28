# JDhruv14/Win-Codex

⭐ 22 · JavaScript · MIT · 推送 2026-03-02 · [GitHub](https://github.com/JDhruv14/Win-Codex) · 个人维护

**在 Windows 上运行 macOS 版 Codex 桌面应用的转换工具**

面向持有 Codex DMG 的 Windows 用户的本地工具：通过 PowerShell 管道（scripts/run.ps1）与交互式终端向导（codex-windows-setup-tool），完成 DMG 解压、为 Electron 兼容性重建/修补原生模块、生成桌面快捷方式并启动应用；支持从 OpenAI 静态地址自动尝试下载 DMG，但不再分发 OpenAI 应用二进制。依赖 Node.js、PowerShell、7-Zip 与全局安装的 Codex CLI，原生模块重编需要 Visual Studio C++ 构建工具链；默认走原生 Windows CLI 路径，WSL 为可选后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解压并修补 DMG 中的原生模块以适配 Electron on Windows
- 交互式向导覆盖 DMG 选择、自动下载、快捷方式与启动选项
- 环境校验命令带自动修复提示，兼容性矩阵逐项标注测试状态
- 默认原生 Windows CLI 路径，WSL 后端需手动验证后可选启用

## 适用场景

- 在没有官方 Windows 版时在 Windows 10/11 上运行 Codex 桌面应用
- 用向导一次性完成 DMG 准备、构建与快捷方式创建
- 出现 EBUSY、原生模块重编失败等问题时按排障指引处理

## 场景标签

 · 领域:开发者工具/桌面应用移植

## 证据(README 行号)

> L3: Run the macOS Codex app DMG on Windows by extracting, patching, and launching it with Windows-compatible native modu
> L5: This project provides a Windows-first setup flow for users who have a Codex DMG and need a repeatable local runner. 
> L24: npm i -g @openai/codex

## 星数曲线

```mermaid
xychart-beta
    title "JDhruv14/Win-Codex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cf70941a834d` · [字段定义](../../DATASET.md)*
