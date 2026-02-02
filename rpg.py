class Hero:
    def __init__(self, name, job, hp, hero_type="hero"):
        self.name = name
        self.job = job
        self.hp = hp
        self.max_hp = hp  # Menyimpan HP awal untuk cek Rage Mode
        self.type = hero_type
        print(f"✨ {self.name} ({self.job}) memasuki arena!")

    def is_alive(self):
        return self.hp > 0


    def serangan(self, musuh):
        # TUGAS 3: Cek status hidup
        if not self.is_alive():
            print(f"❌ {self.name} sudah gugur dan tidak bisa menyerang!")
            return
        

    

    

        # TUGAS 4: Logika Role untuk Damage
        damage = 0
        if self.job == "Warrior":
            damage = 250
        elif self.job == "Mage":
            damage = 190
        elif self.job == "Monster": 
            damage = 220
        elif self.job == "Boss":
            damage = 300
        
        
        # TUGAS 5: Boss Rage Mode (Critical Hit)
        if self.type == "boss" and self.hp <= (self.max_hp / 4):
            print(f"😈 {self.name} memasuki RAGE MODE! Serangan menjadi kritis!")
            damage *= 2 # Damage meningkat 2x lipat

        # Kirim damage ke musuh
        print(f"⚔️ {self.name} menyerang {musuh.name}!")
        musuh.take_damage(damage)



    def ultimate(self, enemy, ):
        dmg = 500
        print(f"⚔️ {self.name} Mengeluarkan skill 1:Lempar tombak!")
        print(f"dengan damege {dmg} DMG")
        # panggil method lain dari dalam
        enemy.take_damage(dmg)

    def amukan(self, enemy, ):
        dmg = 700
        print(f"⚔️ {self.name} 👹👹 AMUKAN RAJA IBLIS: TEKANAN DOMMONS GOD😈😈!")
        print(f"dengan damege {dmg} DMG")
        # panggil method lain dari dalam
        enemy.take_damage(dmg)
        
    def raungan(self, enemy, ):
        dmg = 500
        print(f"⚔️ {self.name} 👹👹 AMUKAN serigal IBLIS: TEKANAN DOMMONS wolf😈😈!")
        print(f"dengan damege {dmg} DMG")
        # panggil method lain dari dalam
        enemy.take_damage(dmg)

    def take_damage(self, damage):
        if damage < 0: damage = 0
        
        self.hp -= damage
        if self.hp < 0: 
            self.hp = 0
            
        print(f"💥 {self.name} menerima {damage} damage. HP tersisa: {self.hp}")
        
        if self.hp == 0:
            print(f"💀 {self.name}  TELAH DIKALAHKAN!!!!!")

    def heal(self, target):
        # TUGAS 3: Cek status hidup
        if not self.is_alive():
            print(f"❌ {self.name} sudah mati, tidak bisa memberikan heal!")
        
            return

        
        # TUGAS 4: Logika Role Healer
        if self.job == "Healer":
            jumlah_heal = 200
            target.hp += jumlah_heal
            if target.hp > target.max_hp: 
                target.hp = target.max_hp
            print(f"💚 {self.name} menyembuhkan {target.name}. HP {target.name} sekarang: {target.hp}")
        else:
            print(f"🚫 {self.name} bukan seorang Healer!")


        



        

# --- TUGAS 6: SIMULASI CERITA ---

print("=== AWAL PERTUALANGAN ===")
# Inisialisasi Party (Tugas 1)
warrior = Hero("Zilong", "Warrior", 1700)
mage = Hero("Alice", "Mage", 1000)
healer = Hero("Estes", "Healer", 1300)

# Musuh Biasa
wolf = Hero("dark wolf", "Monster", 1000, "normal")


print("\n--- PERTEMPURAN MELAWAN dark wolf---")
warrior.serangan(wolf)
mage.serangan(wolf) 
wolf.serangan(warrior)
wolf.serangan(mage)
warrior.ultimate(wolf)




print("\n--- PERTEMPURAN MELAWAN RAJA IBLIS ---")
boss = Hero("Raja Iblis", "Boss", 2500, "boss")

# Hero menyerang Boss sampai HP Boss < 50%
boss.serangan(warrior)
mage.serangan(boss)
mage.serangan(boss)
healer.heal(warrior)

warrior.ultimate(boss)




# Boss masuk Rage Mode (HP 2000 -> 100 atau kurang)
print("\n--- STATUS KRITIS ---")
boss.serangan(mage) # Serangan biasa jika HP masih > 100
healer.heal(mage)
mage.serangan(boss) # Menjatuhkan HP Boss ke area Rage Mode
boss.serangan(warrior) # Menampilkan pesan Rage Mode & Damage Kritis



print("\n=== 👹👹raid makin mengerikan karena boss marah ===")
boss.amukan(warrior)
healer.heal(warrior)
mage.serangan(boss)
boss.serangan(mage)
warrior.ultimate(boss)
mage.serangan(boss)
mage.serangan(boss)
wolf.raungan(warrior)
wolf.raungan(mage)
wolf.raungan(healer)
warrior.serangan(wolf)
warrior.ultimate(boss)
print("\n=======KEMENANGAN UNTUK UMAT MANUSIA==============")


print("\n================ selesai =========================")
