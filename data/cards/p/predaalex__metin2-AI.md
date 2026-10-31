# predaalex/metin2-AI

⭐ 14 · Python · 推送 2026-08-30 · [GitHub](https://github.com/predaalex/metin2-AI) · 个人维护

**Metin2 游戏自动挖矿脚本：OpenCV+Tesseract 检测拾取矿石**

用 Python 编写的 Metin2 游戏挂机脚本，通过 OpenCV 屏幕检测与 Tesseract OCR 识别画面，自动攻击矿石并拾取掉落物；支持同时操作最多 6 个游戏客户端。使用要求：游戏以 800x600 分辨率非全屏窗口排列，可执行文件需以管理员身份运行，按 Q 停止。规划中的功能（小地图寻矿、自动换线）尚未实现。依赖 Python 3.9.x、pip 与 Tesseract，需在代码中指定 tesseract.exe 路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenCV 屏幕检测与 Tesseract OCR 驱动的自动挖矿
- 支持同时运行最多 6 个游戏客户端
- 以管理员权限运行，Q 键停止

## 适用场景

- 挂机自动攻击矿石并拾取掉落物
- 多开客户端批量挖矿

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: I have created a metin2 AI that helps farming. The AI will automatically pick up the ores from the ground and start 
> L7: `python 3.9.x`, `pip` and `tesseract`

## 星数曲线

```mermaid
xychart-beta
    title "predaalex/metin2-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3bdbfd020ffc` · [字段定义](../../DATASET.md)*
