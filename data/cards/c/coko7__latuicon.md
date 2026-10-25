# coko7/latuicon

⭐ 56 · Rust · MIT · 推送 2026-09-22 · [GitHub](https://github.com/coko7/latuicon) · 个人维护

**终端里的图标选择器：emoji/颜文字/Unicode/Nerd Font**

用 Rust 编写的终端 UI（TUI）图标选择工具，从 late.sh 内嵌的 icon picker 组件衍生而来。提供 Emoji、Kaomoji、Unicode 符号与 Nerd Font 字形四类图标的选择页签，按 Enter 将选中图标输出到 stdout，按 Esc 退出。搜索支持模糊匹配与 Unicode 十六进制/名称查找，可通过 config.toml 配置主题、页签、默认页签与自定义颜文字列表。安装途径包括 Nix、Cargo、AUR 与源码脚本构建，跨 Linux/macOS/Windows 配置路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类图标页签（Emoji/Kaomoji/Unicode/Nerd Font）及合并搜索的 All 页签
- 搜索支持模糊匹配（Levenshtein 回退）与 U+XXXX 十六进制、Unicode 名称查找
- config.toml / CLI / 环境变量多级配置，支持 6 种主题与自定义颜文字列表
- 提供 Nix/Cargo/AUR/源码脚本多种安装方式

## 适用场景

- 在终端中快速查找并输出 emoji 或颜文字
- 通过 Hyprland 等桌面绑定呼出悬浮选择器并复制到剪贴板
- 查找 Unicode 符号或 Nerd Font 字形用于配置文件与状态栏

## 场景标签

 · 领域:开发者工具/终端应用

## 证据(README 行号)

> L3: `latuicon`, the **lat**e **TUI** **icon** picker: a rip-off of the late.sh embedded icon picker.
> L12: A terminal UI icon picker for emoji, kaomoji, Unicode characters, and Nerd Font glyphs. Press Enter to print the se

## 星数曲线

```mermaid
xychart-beta
    title "coko7/latuicon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-25 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `28896d1b0bb6` · [字段定义](../../DATASET.md)*
